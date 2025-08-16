from rest_framework import serializers
from .models import Thread, Message


class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = ("id", "project", "participants", "created_at")
        read_only_fields = ("participants", "created_at")


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ("id", "thread", "sender", "body", "created_at")
        read_only_fields = ("sender", "created_at")
