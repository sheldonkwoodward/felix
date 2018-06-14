# sheldon woodward
# 6/13/18

from django.urls import path

from . import views

urlpatterns = [
    path('', views.test_req, name='test_req'),
]
