from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower


class FollowerSerializers(serializers.ModelSerializer):

    follower = serializers.ReadOnlyField(source='follower.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='follower.profile.id')
    profile_image = serializers.ReadOnlyField(source='follower.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.follower

    class Meta:
        model = Follower
        fields = [
            'id', 'follower', 'is_owner', 'profile_id', 'profile_image',
            'following', 'created_at', 'updated_at'
        ]