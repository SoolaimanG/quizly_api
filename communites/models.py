from django.db import models
from base.models import User, Quiz, Category


import uuid

class DateTimeField(models.Model):
 created_at = models.DateTimeField(auto_now_add=True)
 updated_at = models.DateTimeField(auto_now=True)
 
 class Meta:
  abstract = True
  
class PostComments(DateTimeField):
 body = models.CharField(max_length=300)
 post = models.ForeignKey('Posts', on_delete=models.CASCADE)
 
 def __str__(self):
  return self.body

class PostImages(DateTimeField):
 image = models.URLField()
 post = models.ForeignKey('Posts', on_delete=models.CASCADE)
 
 def __str__(self):
  return self.post.title

# Create your models here.
class Posts(DateTimeField):
 posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted_by')
 likes = models.ManyToManyField(User, related_name='likes')
 is_quiz = models.BooleanField(default=False)
 quiz = models.ForeignKey(Quiz, null=True, blank=True, on_delete=models.CASCADE)
 caption = models.CharField(max_length=500, null=True, blank=True)
 
 def __str__(self):
  return self.posted_by.username


class Community(DateTimeField):
 id = models.UUIDField(primary_key=True, default=uuid.uuid4)
 participants = models.ManyToManyField(User)
 posts = models.ManyToManyField(Posts, blank=True)
 requests = models.ManyToManyField(User, related_name='requests', blank=True)
 name = models.TextField(max_length=200)
 description = models.CharField(max_length=500, null=True, blank=True)
 display_picture = models.URLField(null=True, blank=True)
 owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner', default=None)
 join_with_request = models.BooleanField(default=True)
 allow_categories = models.ManyToManyField(Category)
 
 @staticmethod
 def check_for_user_communities(user: User, name: str):
        # Check if a community with the given name already exists
        if Community.objects.filter(name__iexact=name).exists():
            raise ValueError("A community with this name already exists.")

        # Check if the user has too many communities
        if Community.objects.filter(owner=user).count() >= 5:
            raise ValueError("Too many communities are associated with this account. (Delete some and proceed).")

 def accept_request(self, user: User):

  self.participants.add(user)
  self.requests.remove(user)
  #Notify the user
  #notify_user_on_community()
  self.save()
 
 def reject_request(self, user: User):
  #Remove from request list and notify user 
  #notify_user_on_community()
  self.requests.remove(user)
  self.save()
 
 def remove_user(self, user: User):
  self.participants.remove(user)
  self.save()
 
 def remove_post(self, post: Posts):
  self.posts.remove(post)
  #notify_user_on_community()
  self.save()
 
 def __str__(self):
  return self.name
 


