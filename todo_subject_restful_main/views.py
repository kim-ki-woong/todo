from django.shortcuts import render
from .models import TodoList
from .serializers import TodoSerializer, TodoDetailSerializer,TodoCreateSerializer
from django.views import View
from django.views import generic
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView


class Todo_subject_restful_main(ListAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer

class Todo_subject_restful_detail(RetrieveAPIView):
    lookup_field = 'no'
    queryset = TodoList.objects.all()
    serializer_class = TodoDetailSerializer

class Todo_subject_restful_update(UpdateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer

class Todo_subject_restful_delete(DestroyAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer

class Todo_subject_restful_create(CreateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoCreateSerializer