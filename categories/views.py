from rest_framework import generics

from .models import Category
from .serializer import CategorySerializer

# Read all
class CategoryListView(generics.ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

# Create, read, Update and delate
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer



