from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("id", "description", "is_completed", "user")
        read_only_fields = ("user",)
