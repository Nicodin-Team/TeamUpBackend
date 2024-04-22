from rest_framework import  status
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.serializers import  PasswordResetSerializer, PasswordRecoverySerializer
from drf_spectacular.utils import extend_schema
from accounts.models import CustomUser, PasswordResetToken
from django.core.mail import send_mail
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from datetime import timedelta, timezone


class PasswordResetAPIView(APIView):
    """
    This API generates token and sends it to user via email for verifacation.
    """
    serializer_class = PasswordResetSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = CustomUser.objects.filter(email=email).first()
            if user:
                # Generate password reset token and send emai
                token_generator = PasswordResetTokenGenerator
                token = token_generator.make_token(user)                
                code = PasswordResetToken(email, token, expiration = timezone.now() + timedelta(hours=1))
                
                # Send token via email here


                return Response({'message': 'Password reset email sent'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'User with this email does not exist'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class PasswordRecoveryAPIView(APIView):
    """
    This API is responsible for validating toke and and reseting the possword of the user.
    it also checks the password match.
    """
    serializer_class = PasswordRecoverySerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            token = serializer.validated_data['token']
            new_password = serializer.validated_data['new_password']
            confirm_password = serializer.validated_data['confirm_password']

            reset_obj = PasswordResetToken.objects.filter(token = token)
            
            if not reset_obj:
                return Response({'message': 'Invalid Token'}, status=status.HTTP_400_BAD_REQUEST)

            if reset_obj.is_expired():
                return Response({'message': 'Token Expired'}, status=status.HTTP_400_BAD_REQUEST)            
            
            user = CustomUser.objects.filter(email=reset_obj.email).first()
            
            if user:
                user.set_password(new_password)
                reset_obj.delete()
                user.save()

                return Response({'message': 'Password Updated'})
            
            return Response({'message': 'No user found'})
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)