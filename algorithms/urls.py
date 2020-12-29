from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('code/<int:code_id>', views.view_code, name='view_code'),
]