from rest_framework import generics

from .models import Customer
from .serializer import CustomerSerializer

# Read all
class CustomerListView(generics.ListCreateAPIView):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer

# Create, read, Update and delate
class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer

