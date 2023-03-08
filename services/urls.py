from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

app_name='services'
api_router=DefaultRouter()
api_router.register(r'',views.ServiceViewSet,'services')
api_router_image=DefaultRouter()
api_router_image.register(r'',views.ImageViewSet,'images')

urlpatterns=[
    path('images/',include(api_router_image.urls))
]
urlpatterns+=api_router.urls

