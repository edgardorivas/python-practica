from django.http import HttpResponse

def iniciando(request):
    return HttpResponse("mi primer mensaje en django")
