from rest_framework import status,viewsets,mixins,generics
from .models import Service,Image
from .serializer import ServiceSerializer,ImageSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class ServiceViewSet(viewsets.GenericViewSet,mixins.UpdateModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.ListModelMixin,mixins.DestroyModelMixin):
    queryset=Service.objects.all()
    serializer_class=ServiceSerializer

#/notes?customer_id=2
@action(detail=False,methods=['get'],url_path=r'categories/(?P<category_id>[^/.]+)')
def get_service_by_categories(self,request,categories):
        services= Service.objects.get(categories__pk__in=categories.split(''))
        serializer= ServiceSerializer(services,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class ImageViewSet(viewsets.GenericViewSet,mixins.UpdateModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.ListModelMixin,mixins.DestroyModelMixin):
    queryset=Image.objects.all()
    serializer_class=ImageSerializer

