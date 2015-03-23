# Main page redirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
# Redirect to login page
def login(request):
    return HttpResponse("Hello, world. You're at the polls index.!!!!!!!!!")


# Redirect to logout page
def logout(request):    
    return render_to_response('templates/main/logout.html')

# Redirect to index page
def index(request):    
    return render_to_response('templates/main/index.html')
