
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from classes_api import api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    #django URLS
    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),

    #API URLS
    path('classrooms/api', api_views.ClassroomListView.as_view(), name='api-classroom-list'),
    path('classrooms/api/<int:classroom_id>/', api_views.ClassroomDetailView.as_view(), name='api-classroom-detail'),
    path('classrooms/api/create', api_views.ClassroomCreateView.as_view(), name='api-classroom-create'),
    path('classrooms/api/<int:classroom_id>/update', api_views.ClassroomUpdateView.as_view(), name='api-classroom-update'),
    path('classrooms/api/<int:classroom_id>/delete', api_views.ClassroomDeleteView.as_view(), name='api-classroom-delete'),


    #authentication URLS
    path('login/', TokenObtainPairView.as_view(), name='api-login'),
    path('register/', api_views.RegisterView.as_view(), name='api-register'),


]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
