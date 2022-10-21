from functools import wraps
from rest_framework.response import Response
def auth_decorator(view):
    @wraps(view)
    def wrap(self,request):
        if not request.user.is_authenticated:
            return Response({"msg":"you have to be logged in"})
        return view(self,request)
    return wrap