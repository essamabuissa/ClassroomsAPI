from django.shortcuts import render
from rest_framework.generics import CreateAPIView , ListAPIView , RetrieveAPIView ,RetrieveUpdateAPIView ,DestroyAPIView
from classes .models import Classroom
from .serializers import ClassroomListSerializer , ClassroomDetailSerializer , ClassroomUpdateSerializer ,RegisterSerializer , ClassroomCreateSerializer

class ClassroomListView(ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomListSerializer

class ClassroomDetailView(RetrieveAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomDetailSerializer
    lookup_field = "id"
    lookup_url_kwarg = "classroom_id"

class ClassroomCreateView(CreateAPIView):
    serializer_class =  ClassroomCreateSerializer

    def perform_create(self,serializer):
        if self.request.user.is_authenticated:
            serializer.save(teacher = self.request.user)


class ClassroomUpdateView(RetrieveUpdateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomUpdateSerializer
    lookup_field = "id"
    lookup_url_kwarg = "classroom_id"

class ClassroomDeleteView(DestroyAPIView):
    queryset = Classroom.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "classroom_id"

class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
