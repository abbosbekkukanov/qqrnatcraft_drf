from rest_framework import serializers
from .models import Banner, Craftsmanship, Craftsmanshiplist, OurTeam, SocialMediaLink

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'
        

class CraftsmanshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Craftsmanship
        fields = '__all__'


class CraftsmanshipListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Craftsmanshiplist
        fields = '__all__'

class OurTeamSerializer(serializers.ModelSerializer):
    class Meta: 
        model = OurTeam
        fields = '__all__'

class SocialMediaLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaLink
        fields = '__all__'