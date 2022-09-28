# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from userauth.serializers import UserRegistrationSerializer, UserLoginSerializer,Personalinfoserializer,UserEducationserializer,UserExprinceserializer,UserProfileImage,UserSkillserializer
from django.contrib.auth import authenticate
from userauth.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated  
from userauth.models import User,ProfileImage,Personalinfo,UserEduacation,UserExprince,UserSkill
from rest_framework.decorators import api_view






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
    def post (self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user != None:
                token = get_tokens_for_user(user)
                return Response({'token':token,'msg':'Login Success'},status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['Email or password is not valid']}},status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

class ProfileView(APIView):
   
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        serializer = UserRegistrationSerializer(request.user)
        data = serializer.data.get('id')
        print(data)

        User_Profile = ProfileImage.objects.get(user= data)
        serializer1 = UserProfileImage(User_Profile)
        print(data)

        User_Personal_Info = Personalinfo.objects.filter(userid = data)
        serializer2 = Personalinfoserializer(User_Personal_Info, many=True)
        print(data)

        User_Education = UserEduacation.objects.filter(userid = data)
        serializer3 = UserEducationserializer(User_Education, many=True)
        print(data)

        User_Exprince = UserExprince.objects.filter(userid = data)
        serializer4 = UserExprinceserializer(User_Exprince, many=True)
        print(data)

        User_Skill = UserSkill.objects.filter(userid = data)
        serializer5 = UserSkillserializer(User_Skill, many=True)
        print(data)

        
        
        return Response({
            'User_Profile':serializer1.data,
            'User_Personal_Info':serializer2.data,
            'User_Education':serializer3.data,
            'User_Exprince':serializer4.data,
            'User_Skill':serializer5.data,
        }, status=status.HTTP_200_OK)

        


class PersonalinfoView(APIView):
   
    permission_classes = [IsAuthenticated]
    def post (self, request, format=None):
        serializer = Personalinfoserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Personal Information has been filled Succesfully'},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=400)

    def put(self, request, id, format=None):
        user= Personalinfo.objects.get(userid=id)
        serializer = Personalinfoserializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Personal Information has been updated Succesfully'},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=400)
    
    def delete(self,request, id, format=None):
        user = Personalinfo.objects.get(userid=id)
        user.delete()
        return Response({'msg':'Personal Information has been deleted Succesfully'},status=status.HTTP_204_NO_CONTENT)







class UserEducationView(APIView):
    def post(self, request, format=None):
        serializer =UserEducationserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Education has been Filled Succesfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


     
    def put(self, request, id, format=None):
        user= UserEduacation.objects.get(userid=id)
        serializer = UserEducationserializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Education has been updated Succesfully'},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        user = UserEduacation.objects.get(userid=id)
        user.delete()
        return Response({'msg':'Education has been deleted Succesfully'},status=status.HTTP_204_NO_CONTENT)



class UserExprinceView(APIView):
    permissiclasses = [IsAuthenticated]
    def post(self,request,format=None):
        serializer =UserExprinceserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Experience has been Filled Succesfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    

    def put(self, request, id, format=None):
        user= UserExprince.objects.get(userid=id)
        serializer = UserExprinceserializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Exprience has been updated Succesfully'},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        user = UserExprince.objects.get(userid=id)
        user.delete()
        return Response({'msg':'Exprience has been deleted Succesfully'},status=status.HTTP_204_NO_CONTENT)






class UserSkillsview(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        serializer =UserSkillserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Skills added Succesfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    
    def put(self, request, id, format=None):
        user= UserSkill.objects.get(userid=id)
        serializer = UserSkillserializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Skils has been updated Succesfully'},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        user = UserSkill.objects.get(userid=id)
        user.delete()
        return Response({'msg':'Skills has been deleted Succesfully'},status=status.HTTP_204_NO_CONTENT)