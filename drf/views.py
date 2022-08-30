from .models import Thing
from .serializers import ThingSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

class ThingList(ListCreateAPIView):
    # Cant use Django ListView bc that uses templates
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer

class ThingDetail(RetrieveUpdateDestroyAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer


