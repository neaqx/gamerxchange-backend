from rest_framework import serializers
from .models import Profile

class ProfileSerializers(serializers.ModelSerializer):
    owner = serializers.ReadonlyField(source='owner.username')

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'bio', 'games', 'image'
            'content', 'name'
        ]