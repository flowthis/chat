from django.http import HttpResponse


def index(request):
    return HttpResponse("Woohooo. You're at the polls index.")