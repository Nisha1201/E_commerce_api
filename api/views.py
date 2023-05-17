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


from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, UserLoginSerializer
from .models import CustomUser
from rest_framework.response import Response

class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    print(serializer_class,"oooooooooooooooooooooooooooooooooooooooooo")

    def post(self, request, *args, **kwargs):
        print(request.data,"nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")
        serializer = self.get_serializer(data=request.data)
        print(serializer,"ttttttttttttttttttttttttttttttttttt")
        serializer.is_valid(raise_exception=True)

        user =  CustomUser.objects.get(username=serializer.validated_data['username'])
        print(user,"rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
        refresh = RefreshToken.for_user(user)
        print(refresh,"jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

