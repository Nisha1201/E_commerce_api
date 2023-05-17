# from rest_framework import generics, permissions
# from rest_framework_simplejwt.tokens import RefreshToken
# from .serializers import UserSerializer
# from .models import CustomUser
# # from django.contrib.auth.models import User
# from rest_framework.response import Response

# class UserRegisterView(generics.CreateAPIView):
#     serializer_class = UserSerializer
    

# class UserLoginView(generics.GenericAPIView):
#     serializer_class = UserSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         print(request.data,"wwwwwwwwwwwwwwwwwwwwwwwwwwww")
#         serializer.is_valid(raise_exception=True)
#         # Retrieve the user instance using the validated data
#         user = CustomUser.objects.get(username=serializer.validated_data['username'])
#         print(user,"uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")
#         refresh = RefreshToken.for_user(user)
#         print(refresh,"rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
#         return Response({
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#         })


from rest_framework import generics, status
from rest_framework.response import Response
# from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, LoginSerializer
from .models import CustomUser

class UserRegisterView(generics.CreateAPIView):
    # permission_classes = [AllowAny]
    serializer_class = UserSerializer

class UserLoginView(generics.GenericAPIView):
    # permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = CustomUser.objects.get(username=serializer.validated_data['username'])
        print(username,"jjjjjjjjjjjjjjjjjjjjjjjjj")
        print(type(username),"llllllllllllllllllllllllll")
        refresh = RefreshToken.for_user(username)
        print(refresh,"ooooooooooooooooooooooooooooooooo")

        return Response({
            'refresh': str(refresh)
,
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
