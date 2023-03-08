from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name='notes'
api_router=DefaultRouter()
api_router.register(r'',views.NoteViewSet,'notes')
urlpatterns=[]
urlpatterns+=api_router.urls

