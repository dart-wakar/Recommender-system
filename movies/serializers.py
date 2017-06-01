from rest_framework import serializers
from movies.models import Movies,Preferences
from django.contrib.auth.models import User

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ('id','title','details','genres')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','first_name','last_name','password')
        write_only_fields = ('password',)

    def create(self,validated_data):
        print("Inside create")
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        user.save()
        return user

class PreferenceSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model = Preferences
        fields = ('id','user','movie_id','created','modified','rating')
