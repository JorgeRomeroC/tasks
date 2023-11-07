from django.shortcuts import render
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from api.models import Tasks
from api.serializers import TasksSerializer


@extend_schema_view(
    list=extend_schema(description='Nos traer todas las tareas.'),
    retrieve=extend_schema(description='Nos trae solo una tarea.'),
    create=extend_schema(description='Nos crea una tarea.'),
    update=extend_schema(description='Nos actualiza una tarea.'),
    destroy=extend_schema(description='Nos elimina una tarea.'),
)
class TasksViewSet(viewsets.ModelViewSet):
    serializer_class = TasksSerializer
    queryset = Tasks.objects.all()
