from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from usuarios.models.usuario_model import CustomUser

from django.http import HttpResponse
import ldap
import os



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['rol'] = user.rol
        return token

    def validate(self, attrs):
        ldap_uri = os.environ.get('LDAP_URI')
        
        ldap_user = "cn=" + attrs['username'] + ",ou=users,dc=panitapp,dc=co"
        ldap_password = attrs['password']

        cnx = ldap.initialize(ldap_uri, bytes_mode=False)

        cnx.bind_s(ldap_user, ldap_password)
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
    last_name = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True, required=True)


    class Meta:
        model = CustomUser
        fields = ('id','email', 'username', 'password', 'rol', 'first_name','last_name' )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance