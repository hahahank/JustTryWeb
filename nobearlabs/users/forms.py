from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import *
 # extend Django's built-in UserCreationForm and UserChangeForm to
 # remove the username field (and optionally add any others that are
 # required)

class CustomUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__(*args, **kargs)
	print ">>>>>>>>",self.fields,"<<<<<<",type(self.fields)
#        del self.fields['email']

    class Meta:
        model = CustomUser
        fields = '__all__'

class CustomUserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(CustomUserChangeForm, self).__init__(*args, **kargs)
	print ">>>>>>>>",self.fields,"<<<<<<",type(self.fields)
#        del self.fields['email']

    class Meta:
        model = CustomUser
        fields = '__all__'
