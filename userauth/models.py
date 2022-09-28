from dataclasses import dataclass
from email.policy import default
from pyexpat import model
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db.models.signals import post_save
from taggit.managers import TaggableManager

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, firstname, lastname,password=None, password2=None):
        """
        Creates and saves a User with the given email, name, password, password2
        """
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            firstname=firstname,
            lastname=lastname,
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, firstname, lastname,password=None ):
        """
        Creates and saves a superuser with the given email, name, tc
        password and password2.
        """
        user = self.create_user(
            email,
            firstname=firstname,
            lastname=lastname,
            password=password,
           
        )
        user.is_admin = True
        user.save(using=self._db)
        return user





# custom user
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname','lastname']
    

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class ProfileImage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userimage= models.ImageField(upload_to='static/', default='static/images.png')
    background_image= models.ImageField(upload_to='static/', default='static/images.png')
    def __str__(self):
        return self.user.firstname

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = ProfileImage.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)


class Personalinfo(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    bio = models.TextField()
    currentlocation = models.CharField(max_length=200)
    pincode = models.IntegerField()
    dob = models.DateField(max_length=8)
    
    LANGUAGE_CHOICES = (
        ('Urdu','Urdu'),
        ('Hindi' , 'Hindi'),
        ('English' , 'English'),
        ('Marathi' , 'Marathi'),
       
    )
    Language = models.CharField(max_length=15 , choices=LANGUAGE_CHOICES )
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    MARITAL_STATUS= (
        ('M', 'Married'),
        ('U', 'Unmarried'),
    )
    maritalstatus = models.CharField(max_length=1, choices=MARITAL_STATUS)

    def __str__(self) :
       return str(self.userid)
    

class UserEduacation(models.Model):
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    EDUCATION = (
        ('SSC', 'SSC'),
        ('HSC', 'HSC'),
        ('Graduation', 'Graduation'),
        ('Any Diploma','Any Diploma')
    )
    education = models.CharField(max_length=255, choices=EDUCATION)
    Sname = models.CharField(max_length=100)
    percentage = models.PositiveIntegerField()
    passingYear = models.DateField()
    
    def __str__(self):
        return str(self.userid)
    
class UserExprince(models.Model):
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    companyname=models.CharField(max_length=100)
    position_in_company = models.CharField(max_length=50)
    years_of_exprince = models.IntegerField()
    data_of_joining = models.DateField(max_length=8)
    data_of_leaving = models.DateField(max_length=8)


    def __str__(self):
        return str(self.userid)


class UserSkill(models.Model):
    userid = models.ManyToManyField(User)
   
    
    tags = TaggableManager()
    def __str__(self):
        return str(self.userid)