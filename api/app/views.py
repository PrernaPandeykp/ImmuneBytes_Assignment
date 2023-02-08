
from django.http import JsonResponse
from django.views import View
from .models import User

class CreateAccountView(View):
    def get(self, request):
        name = request.GET.get("name")
        email = request.GET.get("email")
        password = request.GET.get("password")
        user = User(name=name, email=email, password=password)
        user.save()

        # Save the user information to the database
        return JsonResponse({"message": "Account created"})

class LoginView(View):
    def put(self, request):
        name = request.PUT.get("name")
        email = request.PUT.get("email")
        password = request.PUT.get("password")
        # Validate the user credentials
        if success:
            # Generate OTP and return it
            return JsonResponse({"status": "success", "otp": 123456})
        else:
            return JsonResponse({"status": "failure"})

class RemoveAccountView(View):
    def delete(self, request):
        name = request.DELETE.get("name")
        email = request.DELETE.get("email")
        password = request.DELETE.get("password")
        # Remove the user account from the database
        return JsonResponse({"message": "Account removed"})


# def create_account(request):
#     name = request.GET.get('name')
#     email = request.GET.get('email')
#     password = request.GET.get('password')

#     # create new account in the database
#     # ...

#     return HttpResponse({"message": "Account created successfully."})

# # def register(request):
# #     if request.method == 'POST':
# #         email = request.POST['email']
# #         password = request.POST['password']
# #         first_name = request.POST['first_name']
# #         last_name = request.POST['last_name']
# #         user = User.objects.create_user(
# #             email=email,
# #             password=password,
# #             first_name=first_name,
# #             last_name=last_name
# #         )
# #         return redirect('login')
# #     return render(request, 'register.html')

# from django.shortcuts import HttpResponse, render
# from django.contrib.auth import authenticate

# def login_user(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         otp = request.POST['otp']

#         user = authenticate(request, email=email, password=password)
#         if user is not None:
#             # Validate the OTP
#             if user.otp == otp:
#                 # Login the user
#                 login(request, user)
#                 return HttpResponse("Login successful.")
#             else:
#                 return HttpResponse("Incorrect OTP.")
#         else:
#             return HttpResponse("Incorrect email or password.")
#     else:
#         return HttpResponse("Invalid request.")

# from rest_framework import generics
# from rest_framework.response import Response
# from rest_framework.permissions import AllowAny
# from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
# from django.contrib.auth import authenticate
# from .serializers import LoginSerializer, RegisterSerializer,OTPSerializer

# class LoginAPIView(generics.GenericAPIView):
#     serializer_class = LoginSerializer
#     permission_classes = [AllowAny]

#     def post(self, request, *args, **kwargs):
#         data = request.data
#         serializer = LoginSerializer(data=data)
#         if serializer.is_valid(raise_exception=True):
#             username = serializer.data['username']
#             password = serializer.data['password']
#             user = authenticate(username=username, password=password)
#             if user:
#                 return Response({'token': user.auth_token.key},
#                                 status=HTTP_200_OK)
#             else:
#                 return Response({'error': 'Wrong credentials'},
#                                 status=HTTP_400_BAD_REQUEST)

# class RegisterAPIView(generics.GenericAPIView):
#     serializer_class = RegisterSerializer
#     permission_classes = [AllowAny]

#     def post(self, request, *args, **kwargs):
#         data = request.data
#         serializer = RegisterSerializer(data=data)
#         if serializer.is_valid(raise_exception=True):
#             user = serializer.save()
#             return Response({
#                 "user": RegisterSerializer(user, context=self.get_serializer_context()).data,
#                 "token": user.auth_token.key
#             }, status=HTTP_200_OK)
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


# class OTPAuthenticationAPIView(generics.GenericAPIView):
#     serializer_class = OTPSerializer
#     permission_classes = [AllowAny]

#     def post(self, request, *args, **kwargs):
#         data = request.data
#         serializer = OTPSerializer(data=data)
#         if serializer.is_valid(raise_exception=True):
#             otp = serializer.data['otp']
#             # Validate the received OTP with the one sent to the user
#             if otp == '1234':  # Example value for demonstration purposes only
#                 # Authenticate the user and generate a token
#                 return Response({'token': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'},
#                                 status=HTTP_200_OK)
#             else:
#                 return Response({'error': 'Invalid OTP'},
#                                 status=HTTP_400_BAD_REQUEST)
