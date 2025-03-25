from django.urls import path
from .views import *
urlpatterns =[
    path('', index, name='home'),
    path('list/', MetroList.as_view(), name='list'),
    path('create/', MetroCreate.as_view(), name='create'),
    path('delete/<int:pk>/', MetroDelete.as_view(), name='delete'),
    path('delete/<int:pk>/', MetroUpdate.as_view(), name='update'),
]