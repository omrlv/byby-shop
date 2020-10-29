from django.urls import path
from . import views

app_name = 'reviews'
urlpatterns = [
    path('', views.reviews, name='reviews'),
    path('leave_review/', views.leave_review, name='leave_review')
]