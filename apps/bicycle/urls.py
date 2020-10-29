from django.urls import path
from . import views

urlpatterns = [
    path('bicycles/<int:id>', views.bicycle_detail_single, name='detail_single'),
    path('bicycles/', views.bicycle_detail_all, name='detail_all'),
]
