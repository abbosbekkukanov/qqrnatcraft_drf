from django.shortcuts import render

from rest_framework import viewsets, generics
from .models import Banner, Craftsmanship, Craftsmanshiplist, SocialMediaLink, OurTeam
from .serializers import BannerSerializer, CraftsmanshipSerializer, CraftsmanshipListSerializer, SocialMediaLinkSerializer, OurTeamSerializer
from .permissions import IsReadOnly 

# Create your views here.


class BannerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsReadOnly]
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class CraftsmanshipViewSet(viewsets.ModelViewSet):
    permission_classes = [IsReadOnly]
    queryset = Craftsmanship.objects.all()
    serializer_class = CraftsmanshipSerializer

class CraftsmanshipListViewSet(viewsets.ModelViewSet):
    permission_classes = [IsReadOnly]
    queryset = Craftsmanshiplist.objects.all()
    serializer_class = CraftsmanshipListSerializer

class OurteamViewSet(viewsets.ModelViewSet):
    permission_classes = [IsReadOnly]
    queryset = OurTeam.objects.all()
    serializer_class = OurTeamSerializer

class SocialMediaLinkViewSet(viewsets.ModelViewSet):
    permission_classes = [IsReadOnly]
    queryset = SocialMediaLink.objects.all()
    serializer_class = SocialMediaLinkSerializer