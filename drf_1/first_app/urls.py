from django.urls import include, path

from . import views

urlpatterns = [
    # path('', views.StudentView.as_view()),
    path('', views.StudentListCreateView.as_view()),
    # path('<int:pk>/', views.StudentDetailView.as_view()),
    path('<int:pk>/', views.StudentRetrieveUpdateDestroyView.as_view()),
]
