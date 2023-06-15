from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.StudentView.as_view()),
    path('<int:pk>/', views.StudentDetailView.as_view()),
]
