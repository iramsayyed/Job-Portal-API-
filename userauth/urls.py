from django.urls import path
from userauth.views import UserRegistrationView,UserLoginView,PersonalinfoView,UserEducationView,UserExprinceView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('peronalinfo/', PersonalinfoView.as_view(), name='peronalinfo'),
    path('education/', UserEducationView.as_view(), name='education'),
    path('experience/', UserExprinceView.as_view(), name='experience'),
    

    
    
    
]
 