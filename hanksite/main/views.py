# Main page redirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, get_object_or_404

# Redirect to login page
def login(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    c = {}
    c.update(csrf(request))    
    return render_to_response('templates/login.html', c)

# Redirect to logout page
def logout(request):    
    return render_to_response('templates/main/logout.html')

# Redirect to index page
def index(request):    
    print "index "
    return render_to_response('templates/main/index.html')
