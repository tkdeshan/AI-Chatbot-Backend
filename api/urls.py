from django.urls import path
from .views import text_gen

urlpatterns = [
    path('chat/', text_gen, name='text_gen'),
]