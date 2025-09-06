from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('profile/', views.profile, name='profile'),
    path('auth/signup/', views.SignUpView.as_view(), name='signup'),
    path('application/all/', views.application_list, name='application_list'),
    path('application/new/', views.create_application, name='create_application'),
    path('application/<int:pk>/', views.application_details, name='application_details'),
    path('application/<int:pk>/edit/', views.edit_application, name='edit_application'),
    path('application/<int:pk>/delete/', views.delete_application, name='delete_application'),
]
