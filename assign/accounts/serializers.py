from .models import User
from rest_framework import serializers

class RoleSerializer(serializers.Serializer):
    role = serializers.CharField()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    roles = RoleSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'nickname',
            'roles',
            'password',
            'password2',
        ]

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password": "Passwords don't match"}
            )

        data.pop('password2')
        return data

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            nickname=validated_data['nickname'],
            role='USER',
        )
        user.set_password(validated_data['password'])
        user.save()
        return {
            'username': user.username,
            'nickname': user.nickname,
            'roles': [{'role': user.role}],
        }
