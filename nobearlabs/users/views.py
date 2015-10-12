from django.views.generic.base import TemplateView,View
from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages


from django.shortcuts import render
from django.views.generic import FormView
from django.contrib import auth 
from .forms import *
from .models import *
from util import forms


class UsersMainView(TemplateView):
    template_name = 'users/userinfo.html'


# Create your views here.
class CreateUserView(FormView):
    template_name = 'usercreate.html'
    form_class = CustomUserCreationForm

    def get_context_data(self, **kwargs):
        print "1. get context data ========================================="
        context = super(CreateUserView, self).get_context_data(**kwargs)
        f = context['form']
        if(f.errors == None):
            print "Data Error"
        else:
            print "2. Get Context  OK"
            if(f.is_bound == True):
                print "[USER] 3. Get data :",f.cleaned_data
	        data = f.cleaned_data
		try:
		    username = data['username']
                    password = data['password1']
                    email =   data['email']

		except:
		    print "Some Error"
		    messages.error(self.request,"Wrong Email format / or Email is used")
		    return 
#		if(password != password2):
#		    messages.warning(self.request, 'PASSWORD NOT SAME')
#		    return  HttpResponseRedirect("/signup2")
	
                print "[USER] 4. acc pw :",username,password,email
                user = CustomUser.objects.create_user(username,email, password)
		print "5. User Create Finish",user
                if(user == None):
                    return HttpResponseRedirect('/login')
                else:
	            print "6. N/E/P/U :",username,email,password,user
                    user = auth.authenticate(username=username, password=password)
                    print "7. user",user," <<<<<< LOGIN RESULT"
                    if user is not None and user.is_active:
                        auth.login(self.request, user)
			print "auth done"
#                        return HttpResponseRedirect('/')
                    else:
			print "auth Done 2"
#                        return HttpResponseRedirect('/login')

                # TODO : 1. check DB with this acc/pw is  Not exist
                # 2. Save To DB
                # 3. auth ok
                '''
                '''
            else:
                print "No data"
        response = context
        print "response:",context
        return False



    def form_valid(self, form):
        print "form valid"
        result = self.get_context_data(form=form)
        # return self.render_to_response(self.get_context_data(form=form))
        if(result==True):
            return HttpResponseRedirect('/')
        else:
            messages.warning(self.request, 'Account or Password not found!!')
            return HttpResponseRedirect('/login')





class LogoutView(View):
    template_name = 'logout.html'
    def get(self, request, *args, **kwargs):
        print  "000 Get Get Get "
        if  self.request.user.is_authenticated():
            auth.logout(self.request)
            messages.info(self.request, 'Bye Bye!')
            return HttpResponseRedirect('/')
        else:
            messages.warning(self.request, 'Please Login first!!')
            return HttpResponseRedirect('/login')

    def post(self, request, *args, **kwargs):
        print  "post post post",request,args
    def head(self, *args, **kwargs):
        last_book = self.get_queryset().latest('publication_date')
        response = HttpResponse('')
        # RFC 1123 date format
        response['Last-Modified'] = last_book.publication_date.strftime('%a, %d %b %Y %H:%M:%S GMT')
        return response


class LoginView(FormView):
    template_name = 'login.html'
    form_class = forms.LoginForm

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        f = context['form']
        if(f.errors == None):
            print "3 Data Error"
        else:
            print "Get Context  OK"
            if(f.is_bound == True):
                username = f.cleaned_data['account']
                password = f.cleaned_data['password']
                print "acc pw :",username,password
                user = auth.authenticate(username=username, password=password)
                print "user",user,"<<<<<< LOGIN RESULT"
                if user is not None and user.is_active:
                    auth.login(self.request, user)
                    return True
                else:
                    return False
            else:
                print "No data"
        response = context
        print "response:",context
        return context

    def form_valid(self, form):
        print "form valid"
        result = self.get_context_data(form=form)
        # return self.render_to_response(self.get_context_data(form=form))
        if(result==True):
            return HttpResponseRedirect('/')
        else:
            messages.warning(self.request, 'Account or Password not found!!')
            return HttpResponseRedirect('/login')

