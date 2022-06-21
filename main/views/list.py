from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from main.models import List, Task
from main.serializers import ListSerializer, TaskSerializer, TaskChangeSerializer
from rest_framework.response import Response


class ListList(generics.ListCreateAPIView, generics.ListAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get(self, request, *args, **kwargs):
        lists = self.get_queryset()
        response = []
        for lst in lists:
            list_dict = {
                'id': lst.id,
                'title': lst.title,
            }

            tasks_response = []
            tasks = Task.objects.filter(list=lst)
            for task in tasks:
                tasks_response.append({
                    'id': task.id,
                    'text': task.text,
                    'status': task.status,
                    'created_at': task.created_at,
                })
            list_dict['tasks'] = tasks_response
            response.append(list_dict)
        return Response(response)


class ListDelete(generics.DestroyAPIView):
    queryset = List.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.queryset.filter(user=self.request.user, pk=self.kwargs['pk']).first()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class TaskDetail(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        lst = List.objects.filter(user=self.request.user, pk=self.kwargs['pk']).first()
        return self.queryset.filter(list=lst)


class TaskChange(generics.DestroyAPIView, generics.UpdateAPIView):
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = TaskChangeSerializer

    def get_object(self):
        return self.queryset.filter(list__user=self.request.user, pk=self.kwargs['pk']).first()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class TaskCreate(generics.CreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
