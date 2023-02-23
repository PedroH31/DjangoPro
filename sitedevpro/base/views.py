from django.shortcuts import render


def home(request):
    return render(request, 'base/home.html', {'contato_email': 'ramalho@python.pro.br'})
