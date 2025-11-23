from django.shortcuts import render
from .models import Jogo

def home(request):
    jogos = Jogo.objects.all()
    return render(request, 'home.html', {'jogos': jogos})

def lista_jogos(request):
    jogos = Jogo.objects.all()
    return render(request, 'posts/jogos.html', {'jogos': jogos})

def jogar(request, jogo_id):
    jogo = Jogo.objects.get(id=jogo_id)
    return render(request, 'posts/jogar.html', {'jogo': jogo})

