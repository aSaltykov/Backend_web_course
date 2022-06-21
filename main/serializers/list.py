from rest_framework import serializers, exceptions
from main.models import List, Task


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ['id', 'title']

    def create(self, validated_data):
        title = validated_data.get('title', '')
        user = self.context['view'].get_object()

        return List.objects.create(
            user=user,
            title=title,
        )


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'list', 'text', 'status']

    def validate_list(self, value):
        user = self.context['view'].get_object()
        if value.user == user:
            return value
        else:
            raise exceptions.ValidationError('Do not have permission')


class TaskChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'text', 'status']

