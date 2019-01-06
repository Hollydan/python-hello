from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def do_map(request):
    return HttpResponse('Hello World !')

def who(request):

    try:
        name = request.GET['name']
        age = request.GET['age']

        return HttpResponse('My name is {} I am {} years old'.format(name, age))
    except Exception as e:
        return e

def who1(request, name, age):
    return HttpResponse('Name: {}, Age: {}'.format(name, age))

def home(request, new_type):
    
    types_dict = {
        'it': 'IT',
        'sport': 'Sport'
    }
    
    return render(request, 'article_home.html', {'new_type': types_dict[new_type] + ' lists'})
