from django.urls import path
from . import views

app_name='customers'

urlpatterns=[
    path('',views.CustomerListView.as_view()),
    path('<int:pk>/',views.CustomerDetailView.as_view()),
]