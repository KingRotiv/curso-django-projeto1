from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(
        request=request,
        template_name='recipes/home.html'
    )


def contact(request):
    return HttpResponse('Contact')


def about(request):
    return HttpResponse('About')
