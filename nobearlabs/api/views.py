from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
 
 
class ApiGet(APIView):
  """
  A custom endpoint for GET request.
  """
  def get(self, request, format=None):
#    return Response({"success": True, "content": "Hello World!1"})
    print "API GET DEMO",request.user.is_authenticated()
    if(request.user.is_authenticated()):
        return Response({"success": True, "content": "Hello World!1"})
    else:
	return Response({"success": False, "content": "Hello World!2"})


