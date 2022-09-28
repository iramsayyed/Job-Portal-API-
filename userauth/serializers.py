from dataclasses import field
from rest_framework import serializers 
from userauth.models import User,Personalinfo,UserEduacation,UserExprince,ProfileImage,UserSkill
from taggit.serializers import TagListSerializerField, TaggitSerializer


class UserRegistrationSerializer(serializers.ModelSerializer):
    # we are writing this becoz we want conformation on resgister
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = User
        fields =['id','email', 'firstname', 'lastname', 'password', 'password2']
        extra_kwargs={
            'password':{'write_only':True}
        }

# validating password and confirm password registartion
    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')
        if password != password2:
            raise serializers.ValidationError("password and confirm password doesn't match ")
        return data

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email','password']


class UserProfileImage(serializers.ModelSerializer):
    class Meta:
        model = ProfileImage
        fields = ['user','userimage','background_image']



class Personalinfoserializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    class Meta:
        model = Personalinfo
        fields = ['userid','name','bio','currentlocation','pincode','dob','Language','gender','maritalstatus']
        
class UserEducationserializer(serializers.ModelSerializer):
    class Meta:
        model = UserEduacation
        fields = ['userid','education','Sname','percentage','passingYear']


class UserExprinceserializer(serializers.ModelSerializer):
    class Meta:
        model = UserExprince
        fields = ['userid','companyname','position_in_company','years_of_exprince','data_of_joining','data_of_leaving']


class UserSkillserializer(TaggitSerializer,serializers.ModelSerializer):
    tags = TagListSerializerField()
    class Meta:
        model = UserSkill
        fields ='__all__'
