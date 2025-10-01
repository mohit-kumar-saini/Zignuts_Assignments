from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Task
import datetime

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password")

    def create(self, validated_data):
        user = User(username=validated_data["username"], email=validated_data.get("email", ""))
        user.set_password(validated_data["password"])
        user.save()
        return user

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ("id", "owner", "created_at", "updated_at")

    def validate_due_date(self, value):
        if value and value < datetime.date.today():
            raise serializers.ValidationError("due_date cannot be in the past.")
        return value
