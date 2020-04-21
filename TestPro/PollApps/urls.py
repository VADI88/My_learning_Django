from .views import news
from django.urls import path

urlpatterns = [
    path('', news ,name='News'),
]

