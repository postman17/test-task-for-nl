from django.urls import path
from .views import PageListView, PageDetailView


urlpatterns = [
    path('', PageListView.as_view()),
    path('<int:pk>/', PageDetailView.as_view()),
]
