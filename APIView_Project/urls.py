
from django.contrib import admin
from django.urls import path
from api.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/drf_test/', DRF_TestAPIView.as_view()),
    path('api/drf_test/<int:pk>/', DRF_TestAPIView.as_view())
]
