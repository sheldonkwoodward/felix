from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('media/', include('media.urls')),
    path('wiki/', include('wiki.urls')),
]
