from django.urls import path
from . import views
from .class_based_views import MessageListView, MessageDetailView

urlpatterns = [
    path('', MessageListView.as_view()),
    path('<int:pk>/', MessageDetailView.as_view(), name='details')
]