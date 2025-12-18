from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User 
from .forms import RegisterForm  # Crie esse formulário para o cadastro de usuários
from .models import Profile
from django.contrib import messages
from django.contrib.auth import logout


from .models import Jogo, Comentario, Curtida

def logout_view(request):
    logout(request)
    messages.success(request, "Você saiu da sua conta.")
    return redirect("home")  # ou "login", se preferir

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
        curtida.delete()

    return redirect(request.META.get("HTTP_REFERER", "home"))

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

def login_cadastro_view(request):
    register_form = RegisterForm()

    if request.method == "POST":

        # ======================
        # LOGIN
        # ======================
        if "login" in request.POST:
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                next_url = request.GET.get("next")
                return redirect(next_url or "home")
            else:
                messages.error(request, "Usuário ou senha inválidos")

        # ======================
        # CADASTRO
        # ======================
        elif "register" in request.POST:
            register_form = RegisterForm(request.POST, request.FILES)

            if register_form.is_valid():
                register_form.save()
                messages.success(request, "Cadastro realizado com sucesso! Faça login.")
                return redirect("login")

    return render(request, 'posts/login_cadastro.html', {
        "register_form": register_form
    })


def lista_jogos(request):
    jogos = Jogo.objects.all()
    return render(request, 'posts/jogos.html', {'jogos': jogos})

def jogar(request, jogo_id):
    jogo = Jogo.objects.get(id=jogo_id)
    return render(request, 'posts/jogar.html', {'jogo': jogo})

