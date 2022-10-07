from django.http import HttpResponse ,JsonResponse, Http404
from .models import TipoUsuario
from django.shortcuts import get_object_or_404

def hello(request , nombre):
    return HttpResponse('hola %s' % nombre)

def registros(request):
    tipos = list(TipoUsuario.objects.values())
    return JsonResponse(tipos,safe=False)

def unRegistro(request, id):
    try:
        #/valor = get_object_or_404(TipoUsuario, id=id)
        valor = TipoUsuario.objects.get(id=id)
        return HttpResponse('el nombre del tipo es : %s' % valor.nombre)
    except TipoUsuario.DoesNotExist:
        raise Http404('no se encontro ')

def eliminar(request, id):
    try:
        valor = TipoUsuario.objects.get(id=id)
        valor.delete()
        return HttpResponse('Se elimino el elemento')
    except TipoUsuario.DoesNotExist:
        raise Http404('no se encontro el elemento a eliminar')