from django.urls import path
from . import views

urlpatterns = [
    path('', views.app, name="app"),
    path('book/<int:pk>/', views.SingleBook.as_view(), name="singleBook")
]