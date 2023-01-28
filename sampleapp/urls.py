from django.urls import path
from sampleapp import views

urlpatterns = [
    path('learndj/',views.learn_django)
]