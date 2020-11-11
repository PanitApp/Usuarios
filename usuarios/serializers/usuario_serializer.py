from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from usuarios.models.usuario_model import CustomUser
from rest_framework_simplejwt.backends import TokenBackend

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        print("holi")
        print(user.email)
        print(user.password)
        # Add custom claims
        token['rol'] = user.rol
        return token

    def validate(self, attrs):
        print(attrs)        
        return super().validate(attrs)

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    email = serializers.EmailField(
        required=True
    )
    username = serializers.CharField(required=True)
    rol = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'rol' )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance