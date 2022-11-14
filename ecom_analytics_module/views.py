from django.http import HttpResponse

def index(request):
    ''' Single View to check whether the server is live or not '''
    return HttpResponse("server is up and running")


