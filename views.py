from django.http import HttpResponse

def index(request):
    return HttpResponse("Pagina index")


def about(request):
    return HttpResponse("Pagina about")

def page1(request):
    return HttpResponse("Pagina page1")
