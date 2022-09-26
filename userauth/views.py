# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from userauth.serializers import UserRegistrationSerializer, UserLoginSerializer,Personalinfoserializer,UserEducationserializer,UserExprinceserializer
from django.contrib.auth import authenticate
from userauth.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated  




# Create your views here.
# Create your views here.
# Geneate token manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
class UserRegistrationView(APIView):
    # renderer_classes = [UserRenderer]
    def post (self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):

            user=serializer.save()

            return Response({'msg':'Registartion Successful'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    renderer_classes = [UserRenderer]
    def post (self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            print(user)
            if user != None:
                token = get_tokens_for_user(user)
                return Response({'token':token,'msg':'Login Success'},status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['Email or password is not valid']}},status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 


class PersonalinfoView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post (self, request, format=None):
        serializer = Personalinfoserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Personal Information has been filled Succesfully'},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=400)


class UserEducationView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer =UserEducationserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Education has been Filled Succesfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)



class UserExprinceView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        serializer =UserExprinceserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Experience has been Filled Succesfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

