from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tasks import api

router = routers.DefaultRouter()
router.register(r'tasks', api.TaskViewSet, basename='task')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('tasks.auth_urls')),
    path('api/', include(router.urls)),
    # serve frontend pages
    path('', include('tasks.frontend_urls')),
]
