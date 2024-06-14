from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

# Creating notes
class NoteListCreate(generics.ListCreateAPIView): #  We have used ListCreateAPIView as it will show the list of the notes or it will create an note
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated] # It's set to authenticated as we want to verify it with authenticated JWT token

    def get_queryset(self): # To use get_queryset insted of queryset as we want to access request object which specifies the user. The functionality is we can see our notes but not the notes notes written by other user
        user = self.request.user # When we want to call user we need to pass it as self
        return Note.objects.filter(author=user) # It will return all the notes written by the user

# This funtion will check the new serializer with the one we created in NoteSerialzer, In NotSerialzer as we have mentioned author is read_only so we have to manually check and add the data
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

# This class deletes the notes
class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

# This function will delete the note made by it's user only. It does my checking the permission_classes which is set to authenticated
    def get_queryset(self): 
        user = self.request.user
        return Note.objects.filter(author=user) 

# Generics in django automatically handles a new objects for us
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny] # AllowAny will allow any user to allow to access this view
