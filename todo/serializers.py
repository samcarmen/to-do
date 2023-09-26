from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("id", "description", "is_completed", "user", "target_date")
        read_only_fields = ("user",)
