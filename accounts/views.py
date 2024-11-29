from rest_framework import status, views
from rest_framework.response import Response
from .models import EmailConfirmation, CustomUser, UserProfile
from .serializers import EmailConfirmationSerializer, ConfirmCodeSerializer, UserProfileSerializer

class RegisterEmailView(views.APIView):
    def post(self, request):
        serializer = EmailConfirmationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Confirmation code sent to your email"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConfirmCodeView(views.APIView):
    def post(self, request):
        serializer = ConfirmCodeSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            confirmation_code = serializer.validated_data['confirmation_code']
            try:
                email_confirmation = EmailConfirmation.objects.get(email=email, confirmation_code=confirmation_code)
                if email_confirmation.is_confirmed:
                    return Response({"message": "Email already confirmed"}, status=status.HTTP_400_BAD_REQUEST)
                email_confirmation.is_confirmed = True
                email_confirmation.save()
                return Response({"message": "Email confirmed, please complete your profile"}, status=status.HTTP_200_OK)
            except EmailConfirmation.DoesNotExist:
                return Response({"error": "Invalid confirmation code"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CompleteProfileView(views.APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            email_confirmation = EmailConfirmation.objects.get(email=email, is_confirmed=True)
        except EmailConfirmation.DoesNotExist:
            return Response({"error": "Email not confirmed"}, status=status.HTTP_400_BAD_REQUEST)

        user = CustomUser.objects.create_user(email=email, password=password)
        profile_serializer = UserProfileSerializer(data=request.data)
        if profile_serializer.is_valid():
            profile_serializer.save(user=user)
            return Response({"message": "Profile created successfully"}, status=status.HTTP_201_CREATED)
        return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
