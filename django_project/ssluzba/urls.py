from django.urls import path
from .views import (
    index,
    professors,
    students
)

urlpatterns = [
    path('', index),
    path('students/', students),
    path('professors/', professors),
]
