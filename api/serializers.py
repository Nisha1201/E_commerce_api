from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from api.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    phone=serializers.IntegerField()
    address=serializers.CharField()
    class Meta:
        model = CustomUser
        fields = ('username', 'password','phone','address','first_name','last_name',)
    


from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from api.models import CustomUser

class UserLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    allowed_methods = ['POST']
    class Meta:
        model = CustomUser
        fields = ('username', 'password')

    def validate(self, attrs):
        username = attrs.get('username')
        print(username,"oooooooooooooooo")
        password = attrs.get('password')

        if username and password:
            user =  CustomUser.objects.get(username=['username'])
        #     if user:
        #         if not user.check_password(password):
        #             raise serializers.ValidationError('Incorrect password')
        #     else:
        #         raise serializers.ValidationError('User not found')
        # else:
        #     raise serializers.ValidationError('Both username and password are required')

        attrs['user'] = user                    
        return attrs
