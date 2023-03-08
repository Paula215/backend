from rest_framework import status,viewsets,mixins
from customers.models import Customer
from .models import Note
from .serializer import NoteByCustomerSerializer, NoteSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class NoteViewSet(viewsets.GenericViewSet,mixins.UpdateModelMixin,mixins.CreateModelMixin):
    queryset=Note.objects.all()
    serializer_class=NoteSerializer

#/notes?customer_id=2
@action(detail=True,methods=['get'],url_path='customers')
def get_notes_by_customer(self,request,pk):
    try:
        customer= Customer.objects.get(pk-pk)
        serializer= NoteByCustomerSerializer(customer)
        return Response(serializer.data)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_200_OK)




