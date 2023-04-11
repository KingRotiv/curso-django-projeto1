from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(
        request=request,
        template_name='recipes/home.html',
        context={
            'name': 'Vitor'
        }
    )


def contact(request):
    return render(
        request=request,
        template_name='recipes/contact.html'
    )


def about(request):
    return HttpResponse('About')
