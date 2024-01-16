from rest_framework import serializers
from typing import Any

#Models Import
from .models import Community

class PopularCommunitiesSerializer(serializers.ModelSerializer):
    participants_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Community
        fields = ['id', 'name', 'display_picture', 'created_at', 'participants_count']
        
    def get_participants_count(self, obj: Any):
     return obj.participants.count()

class ImageSerializer(serializers.ModelSerializer):
   image = serializers.ImageField()
