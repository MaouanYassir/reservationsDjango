
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('catalogue/', include('catalogue.urls')),
    path('admin/', admin.site.urls),
]
