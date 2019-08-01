from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', views.UsersViewSet)
router.register('projects', views.ProjectsViewSet)
router.register('tasks', views.TasksViewSet)


urlpatterns = [
    path('', include(router.urls))
]
