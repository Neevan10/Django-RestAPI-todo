from django.conf.urls import url
from django.urls import path, include
from .views import (
    TodoDetailApiView,
)

urlpatterns = [
    path('api/<int:todo_id>/', TodoDetailApiView.as_view()),
]