from django.urls import path
from .views import RegisterEmailView, ConfirmCodeView, CompleteProfileView

urlpatterns = [
    path('register/email/', RegisterEmailView.as_view(), name='register_email'),
    path('register/confirm/', ConfirmCodeView.as_view(), name='confirm_code'),
    path('register/complete/', CompleteProfileView.as_view(), name='complete_profile'),
]