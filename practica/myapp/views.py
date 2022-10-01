from django.http import HttpResponse

def holaMundo(request):
    return HttpResponse("hola a mi mundo")
