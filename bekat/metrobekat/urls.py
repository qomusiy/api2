from django.urls import path
from .views import *
urlpatterns =[
    path('', index, name='home'),
    path('listview/', MetroBekatView.as_view(), name='listview'),
    path('createview/', MetroCreateView.as_view(), name='createview'),
    path('updateview/<int:pk>/', MetroUpdateView.as_view(), name='updateview'),
    path('deleteview/<int:pk>/', MetroBekatDeleteView.as_view(), name='deleteview'),
    path('detailview/<int:pk>/', MetroBekatDetailView.as_view(), name='detailview'),
    
    # path('list/', MetroList.as_view(), name='list'),
    # path('create/', MetroCreate.as_view(), name='create'),
    # path('delete/<int:pk>/', MetroDelete.as_view(), name='delete'),
    # path('delete/<int:pk>/', MetroUpdate.as_view(), name='update'),
    # path('listcreate/', MetroListCreate.as_view(), name='listcreate'),
    # path('retrievedelete/<int:pk>/', MetroRetrieveDestroy.as_view(), name='destroyretrieve'),
]


###  viewset'ning url kodi, tepadagi kodni kommentga olib buni ishlatiladi

# from .views import MetroViewSet
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'bekats', MetroViewSet, basename='bekat')
# urlpatterns = router.urls