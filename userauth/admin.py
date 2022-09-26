from django.contrib import admin
from userauth.models import User,ProfileImage,Personalinfo,UserEduacation,UserExprince
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
class UserModelAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.
    list_display = ('id','email', 'firstname','lastname', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('User Credentials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('firstname','lastname')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'firstname', 'lastname', 'password1', 'password2'),
        }),
    )
    search_fields = ('email','firstname','lastname')
    ordering = ('email','id')
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(User, UserModelAdmin)
admin.site.register(ProfileImage)
admin.site.register(Personalinfo)
admin.site.register(UserEduacation)
admin.site.register(UserExprince)
# admin.site.register(UserSkills)







