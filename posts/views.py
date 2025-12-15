from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from .models import Jogo, Comentario, Curtida

def home(request):
    jogos = Jogo.objects.all()
    return render(request, 'home.html', {'jogos': jogos})

def detalhes_jogo(request, jogo_id):
    jogo = get_object_or_404(Jogo, id=jogo_id)
    comentarios = Comentario.objects.filter(jogo=jogo)
    curtido = False

    if request.user.is_authenticated:
        curtido = Curtida.objects.filter(jogo=jogo, usuario=request.user).exists()

    return render(request, "posts/jogo_detalhes.html", {
        "jogo": jogo,
        "comentarios": comentarios,
        "curtido": curtido,
    })

@login_required
def curtir(request, jogo_id):
    jogo = get_object_or_404(Jogo, id=jogo_id)

    curtida, created = Curtida.objects.get_or_create(
        usuario=request.user,
        jogo=jogo
    )

    if not created:  
        curtida.delete()  # descurtir

    return redirect("home")

@login_required
def comentar(request, jogo_id):
    jogo = get_object_or_404(Jogo, id=jogo_id)

    if request.method == "POST":
        texto = request.POST.get("comentario")
        Comentario.objects.create(
            jogo=jogo,
            usuario=request.user,
            texto=texto
        )
        return redirect("jogo_detalhes", jogo_id=jogo.id)

    return render(request, "posts/comentar.html", {"jogo": jogo})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def lista_jogos(request):
    jogos = Jogo.objects.all()
    return render(request, 'posts/jogos.html', {'jogos': jogos})

def jogar(request, jogo_id):
    jogo = Jogo.objects.get(id=jogo_id)
    return render(request, 'posts/jogar.html', {'jogo': jogo})

