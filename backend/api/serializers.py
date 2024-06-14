from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}
    
    # Creating a method to use new version of the user. In this fuction the validated_data varible checks with the model 'User'. 
    # It checks all the fields in the model and then creates an new user. 
    # The '**' splits the key value pair in the dictionary used in password/model
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user 
    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields  = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}} # Keeping it to read only beacuse we want to define who the author is 