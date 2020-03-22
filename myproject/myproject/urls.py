from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('urls/', include('urls')),
    path('admin/', admin.site.urls),
]
