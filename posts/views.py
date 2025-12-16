from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User 
from .forms import RegisterForm  # Crie esse formulário para o cadastro de usuários
from .models import Profile
from django.contrib import messages


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
    login_form = AuthenticationForm()
    register_form = RegisterForm()

    if request.method == "POST":
        action = request.POST.get("action")

        # LOGIN
        if action == "login":
            login_form = AuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                messages.success(request, "Login realizado com sucesso!")
                return redirect("home")

        # CADASTRO
        elif action == "register":
            register_form = RegisterForm(request.POST, request.FILES)
            if register_form.is_valid():
                user = register_form.save()

                # Atualiza o profile criado pelo receiver
                profile = user.profile
                profile.bio = register_form.cleaned_data.get("bio")
                profile.foto = register_form.cleaned_data.get("foto")
                profile.save()

                login(request, user)
                messages.success(request, "Cadastro realizado com sucesso! 🎉")
                return redirect("home")

    return render(
        request,
        "login_cadastro.html",
        {
            "login_form": login_form,
            "register_form": register_form,
        },
    )

def lista_jogos(request):
    jogos = Jogo.objects.all()
    return render(request, 'posts/jogos.html', {'jogos': jogos})

def jogar(request, jogo_id):
    jogo = Jogo.objects.get(id=jogo_id)
    return render(request, 'posts/jogar.html', {'jogo': jogo})

def login_cadastro_view(request):
    # Inicializa ambos os forms, garantindo que sempre existam
    form = AuthenticationForm()
    register_form = RegisterForm()

    if request.method == 'POST':
        # Verifica se veio do botão de login
        if request.POST.get('action') == 'login':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('home')

        # Verifica se veio do botão de cadastro
        elif request.POST.get('action') == 'register':
            register_form = RegisterForm(request.POST, request.FILES)
            if register_form.is_valid():
                user = register_form.save()
                # Cria profile com foto e bio
                foto = request.FILES.get('foto')
                bio = request.POST.get('bio')
                Profile.objects.create(user=user, foto=foto, bio=bio)
                login(request, user)
                return redirect('home')

    return render(request, 'posts/login_cadastro.html', {'form': form, 'register_form': register_form})