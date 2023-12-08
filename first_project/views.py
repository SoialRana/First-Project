from django.http import HttpResponse

def home(request):
    return HttpResponse("this is my first django project")



def about(request):
    return HttpResponse("this is my about page")