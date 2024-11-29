from rest_framework import serializers
from .models import CustomUser, UserProfile, EmailConfirmation
from .utils import send_confirmation_email

class EmailConfirmationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailConfirmation
        fields = ['email']

    def create(self, validated_data):
        email = validated_data['email']
        email_confirmation, created = EmailConfirmation.objects.get_or_create(email=email)
        email_confirmation.generate_confirmation_code()
        send_confirmation_email(email, email_confirmation.confirmation_code) #- Bu joyda email yuborish funksiyasini chaqiring
        return email_confirmation

class ConfirmCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    confirmation_code = serializers.CharField(max_length=6)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_image', 'address', 'latitude', 'longitude', 'phone_number']
