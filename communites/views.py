
#Rest Framework Import
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

#Django Imports
from django.db import models
from django.shortcuts import get_object_or_404

#Base Imports
from .models import Community, User

#Serializers Import
from .serializers import PopularCommunitiesSerializer, ImageSerializer

from helpers import image_uploader


@api_view(['GET'])
def get_communities(request, size: str):
 try:
  data = request.query_params
  #popular = data.get('popular', False)
  
  size = int(size)
  
  user: User = request.user
  print(user)

  communities = Community.objects.annotate(most_participants=models.Count('participants'), most_post=models.Count('posts'))
   
  if user.is_authenticated: #Exclude the community the current user is is in
    communities = communities.exclude(participants=user)
    
  communities = communities.order_by('-most_participants','-most_post')[:size]

  data = PopularCommunitiesSerializer(communities, many=True)
   
  return Response({'data':data.data,'message':'OK'},status=status.HTTP_200_OK)
   #here we are only going to return the [name, participants_count, display_image, if]
 except Exception as e:
  return Response({'data':{},'message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def join_or_leave_community(request):
 try:
  
  user:User = request.user
  community_id = request.query_params.get('community_id')
  
  try:
   community = Community.objects.get(id=community_id)
  except Community.DoesNotExist:
   return Response({'data':{},'message':'Community with this ID does not exist'},status=status.HTTP_404_NOT_FOUND)
  
  is_already_a_member = community.participants.filter(id=user.id).exists()
  in_queue_for_approval = community.requests.filter(id=user.id).exists()
  
  if in_queue_for_approval:
   #Cancel Request
   community.requests.remove(user)
   community.save()
   return Response({'data':{},'message':'Your request has been canceled'},status=status.HTTP_200_OK)
  
  if is_already_a_member:
   #If user is already a member then remove the user
   community.participants.remove(user)
   community.save()
   return Response({'data':{},'message': f'You just left {community.name}'},status=status.HTTP_200_OK)
  
  if community.join_with_request:
   community.requests.add(user)
   community.save()
   return Response({'data':{},'message':'Request has been sent to this community admin for processing.'},status=status.HTTP_200_OK)
 
  community.participants.add(user)
  community.save()
  
  return Response({'data':{},'message':f'You joined {community.name}'},status=status.HTTP_200_OK)
  
 except Exception as e:
  return Response({'data':{},'message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 
#@permission_classes([IsAuthenticated])
@api_view(['GET'])
def am_i_a_community_member(request):
 try:
  user:User = request.user
  
  if user.is_authenticated:
   community_id = request.query_params['community_id']
  
   community = get_object_or_404(Community, id=community_id)
  
   is_member = community.participants.filter(id=user.id).exists()
   is_requested = community.requests.filter(id=user.id).exists()
   data = {'is_member': is_member, 'is_requested': is_requested}
   #print(data)
  else:
   data = {'is_member': False, 'is_requested': False}
  
  return Response({'data': data ,'message':'OK'},status=status.HTTP_200_OK)
  
 except Exception as e:
  return Response({'data':{},'message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 
class MyCommunity(APIView):
 #Get Community Posts
 def get(self, request):
  pass
 
 # Create Community..
 @permission_classes([IsAuthenticated])
 def post(self, request):
  
  try:
   
   user:User = request.user #Current user...
  
   data = request.data
   banner = data['banner']
   name = data['name']
   allow_categories = data['categories']
   description = data.get('description', '')
   join_with_request = data.get('join_with_request', False)
  
   community = Community.objects.create(
    name=name,
    description=description,
    display_picture='',
    owner=user,
    join_with_request=join_with_request,
   )
  
   community.allow_categories.set(allow_categories)
   community.participants.add(user)
  
   community.save()

   return Response({'data':{},'message':"OK"}, status=status.HTTP_200_OK)

  except Exception as e:
   return Response({'data':{},'message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 
 
 #Edit your post
 def patch(self, request):
  pass
 
 #Delete Post on Community -->If you are the on that posted it
 def delete(self, request):
  pass
 

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_community(request):
 from base.models import Category
 try:
  user: User = request.user

  data = request.data
  name = data['name']
  allow_categories = data["allow_categories"]
  description = data.get('description', '')
  display_picture = data.get('display_image')
  join_with_request = data.get('join_with_request', False)

  allow_categories = allow_categories.split(',')
  join_with_request = join_with_request.capitalize()

  Community.check_for_user_communities(user=user, name=name) #This will check if the user has too many communities or if the community with this name already exists.


  image = image_uploader(display_picture) #Upload image to server -->Return a URL

  community = Community(
   name=name,
   owner=user,
   description=description, 
   join_with_request=join_with_request,
   display_picture = image
  )

  # # Find the category and add it.
  categories = Category.objects.filter(body__in=allow_categories)
  community.save()
  community.allow_categories.set(categories)
  
  community.participants.add(user)
  
  community.save()

  return Response({'data':{},"message":'OK'},status=status.HTTP_200_OK)
 except Exception as e:
  print(e)
  return Response({'data':{},"message":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ManageMyCommunity(APIView):
 def post(self, request):
  pass
