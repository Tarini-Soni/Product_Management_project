from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "API is running"})

urlpatterns = [
    path('', home),

    path('admin/', admin.site.urls),

    path('api/auth/', include('auth_app.urls')),
    path('api/', include('projects.urls')),
    path('api/', include('tasks.urls')),
    path('api/', include('comments.urls')),
]