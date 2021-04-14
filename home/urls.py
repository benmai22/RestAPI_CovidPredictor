from django.urls import path,include
from .views import *
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('MyAPI', views.ApprovalsView)

urlpatterns = [
    path('api/', include(router.urls)),
    path('status/', views.corona),
    path('',current_datetime),
   
]