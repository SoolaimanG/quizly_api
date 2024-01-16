from django.urls import path
from . import views

urlpatterns = [
 path('get-communities/<str:size>/', views.get_communities, name='get_communities'),
 path('am-i-a-member/', views.am_i_a_community_member, name='am_i_a_community_member'),
 path('join-or-leave-community/', views.join_or_leave_community, name='join_or_leave_community'),
 path("create-community/",views.create_community, name="create_community"),
]