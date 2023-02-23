from django.http import HttpResponse


def Hello_World(request):
    return HttpResponse('안녕하세요')