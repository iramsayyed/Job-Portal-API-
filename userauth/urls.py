from django.urls import path
from userauth.views import UserRegistrationView,UserLoginView,PersonalinfoView,UserEducationView,UserExprinceView,ProfileView,UserSkillsview 

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profileview/', ProfileView.as_view(), name='peronalinfo'),
    path('peronalinfo/', PersonalinfoView.as_view(), name='peronalinfo'),
    path('peronalinfo/<int:id>', PersonalinfoView.as_view(), name='peronalinfo'),
    path('education/', UserEducationView.as_view(), name='education'),
    path('education/<int:id>', UserEducationView.as_view(), name='education'),
    path('experience/', UserExprinceView.as_view(), name='experience'),
    path('experience/<int:id>', UserExprinceView.as_view(), name='experience'),
    path('skills/', UserSkillsview.as_view(), name='skils'),
    path('skills/<int:id>', UserSkillsview.as_view(), name='skils'),
    
    

    
    
    
]
 