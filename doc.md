http://127.0.0.1:8000/
http://127.0.0.1:8000/lista/
http://127.0.0.1:8000/jogar/2

ao clonar

- criar venv

- instalar o django

- Migrar o banco de dados

  Execute no terminal (na pasta do projeto, onde está manage.py):
  
  python manage.py migrate
  
- python inserir_jogos.py 

Rodar o servidor
python manage.py runserver


--------------------------------------------------------------------------------------------

0. Criar pasta do projeto

mkdir blog 
cd blog

1. Criar um ambiente virtual 

python -m venv venv

2. Ativar o ambiente virtual 

venv\Scripts\activate 

use para desativar

deactivate

erro: execução de scripts foi desabilitada neste sistema.

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
venv\Scripts\activate

3. Instale o Django com a venv ativa  

pip install django

4. Criar projeto Django

 django-admin startproject blog . (o ponto final evita criação de subpasta extra)

Foram criados:
blog/manage.py 
    - init 
    - asgi 
    - settings 
    - urls 
    - wsgi 
    - manage
    

5. Criar um app chamado posts

na pasta raiz 
python manage.py startapp posts

5.1  Adicionar o app no settings.py

    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'posts',  # ← adiciona aqui
]

5.1.1 Crie um arquivo chamado inserir_jogos.py dentro da pasta do projeto, no mesmo nível de manage.py.

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
django.setup()

from posts.models import Jogo

jogos = [
    {
        "nome": "🐍 Jogo da Cobrinha (Snake Game)",
        "descricao": "Um jogo clássico onde você controla uma cobrinha que cresce ao comer frutas.",
        "codigo": """<canvas id='snake' width='400' height='400'></canvas>
<script>
const canvas = document.getElementById('snake');
const ctx = canvas.getContext('2d');
let box = 20;
let snake = [{x: 9 * box, y: 10 * box}];
let direction = 'RIGHT';
let food = {x: Math.floor(Math.random()*19+1)*box, y: Math.floor(Math.random()*19+1)*box};

document.addEventListener('keydown', directionHandler);

function directionHandler(event) {
  if (event.keyCode == 37 && direction != 'RIGHT') direction = 'LEFT';
  else if (event.keyCode == 38 && direction != 'DOWN') direction = 'UP';
  else if (event.keyCode == 39 && direction != 'LEFT') direction = 'RIGHT';
  else if (event.keyCode == 40 && direction != 'UP') direction = 'DOWN';
}

function draw() {
  ctx.fillStyle = '#111';
  ctx.fillRect(0, 0, 400, 400);

  for (let i = 0; i < snake.length; i++) {
    ctx.fillStyle = i == 0 ? '#0f0' : '#fff';
    ctx.fillRect(snake[i].x, snake[i].y, box, box);
  }

  ctx.fillStyle = '#f00';
  ctx.fillRect(food.x, food.y, box, box);

  let snakeX = snake[0].x;
  let snakeY = snake[0].y;

  if (direction == 'LEFT') snakeX -= box;
  if (direction == 'UP') snakeY -= box;
  if (direction == 'RIGHT') snakeX += box;
  if (direction == 'DOWN') snakeY += box;

  if (snakeX == food.x && snakeY == food.y) {
    food = {x: Math.floor(Math.random()*19+1)*box, y: Math.floor(Math.random()*19+1)*box};
  } else {
    snake.pop();
  }

  let newHead = {x: snakeX, y: snakeY};
  if (snakeX < 0 || snakeY < 0 || snakeX >= 400 || snakeY >= 400) clearInterval(game);
  snake.unshift(newHead);
}

let game = setInterval(draw, 100);
</script>"""
    },
    {
        "nome": "🧠 Jogo da Memória",
        "descricao": "Combine os pares de emojis o mais rápido possível.",
        "codigo": """<div id='tabuleiro'></div>
<script>
const emojis = ['😀','😀','🐍','🐍','🎮','🎮','👾','👾'];
let embaralhado = emojis.sort(() => 0.5 - Math.random());
let selecionadas = [];
let tabuleiro = document.getElementById('tabuleiro');
tabuleiro.style.display = 'grid';
tabuleiro.style.gridTemplateColumns = 'repeat(4, 60px)';
tabuleiro.style.gap = '10px';

embaralhado.forEach((emoji, i) => {
  let carta = document.createElement('button');
  carta.textContent = '?';
  carta.style.fontSize = '30px';
  carta.onclick = () => {
    if (selecionadas.length < 2 && carta.textContent == '?') {
      carta.textContent = emoji;
      selecionadas.push({emoji, carta});
      if (selecionadas.length === 2) {
        if (selecionadas[0].emoji === selecionadas[1].emoji) {
          selecionadas = [];
        } else {
          setTimeout(() => {
            selecionadas.forEach(c => c.carta.textContent = '?');
            selecionadas = [];
          }, 800);
        }
      }
    }
  };
  tabuleiro.appendChild(carta);
});
</script>"""
    },
    {
        "nome": "🏓 Jogo Pong",
        "descricao": "Versão simples do clássico Pong, com IA básica e movimento do jogador.",
        "codigo": """<canvas id='pong' width='400' height='300'></canvas>
<script>
const canvas = document.getElementById('pong');
const ctx = canvas.getContext('2d');
let player = {x: 10, y: 100, w: 10, h: 80};
let ai = {x: 380, y: 100, w: 10, h: 80};
let ball = {x: 200, y: 150, r: 10, dx: 3, dy: 3};

function drawRect(x,y,w,h,c){ctx.fillStyle=c;ctx.fillRect(x,y,w,h);}
function drawCircle(x,y,r,c){ctx.fillStyle=c;ctx.beginPath();ctx.arc(x,y,r,0,Math.PI*2);ctx.closePath();ctx.fill();}
canvas.addEventListener('mousemove', e=>player.y=e.offsetY-player.h/2);

function update(){
  ball.x+=ball.dx; ball.y+=ball.dy;
  if(ball.y+ball.r>canvas.height||ball.y-ball.r<0)ball.dy*=-1;
  if(ball.x-ball.r<player.x+player.w && ball.y>player.y && ball.y<player.y+player.h)ball.dx*=-1;
  if(ball.x+ball.r>ai.x){ai.y=ball.y-ai.h/2; ball.dx*=-1;}
}

function render(){
  drawRect(0,0,400,300,'#111');
  drawRect(player.x,player.y,player.w,player.h,'#0f0');
  drawRect(ai.x,ai.y,ai.w,ai.h,'#0f0');
  drawCircle(ball.x,ball.y,ball.r,'#fff');
}

function game(){update();render();}
setInterval(game,30);
</script>"""
    }
]

Jogo.objects.all().delete()
for jogo in jogos:
    Jogo.objects.create(**jogo)

print("✅ Jogos inseridos com sucesso!")

5.1.2 Executar o script para popular o banco

python inserir_jogos.py 

Saída esperada:
✅ Jogos inseridos com sucesso!


5.2 Criar o modelo Post

    from django.db import models

    class Jogo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    codigo = models.TextField()

    def __str__(self):
        return self.nome
    
5.3 Migrar o banco de dados

Execute no terminal (na pasta do projeto, onde está manage.py):
python manage.py makemigrations
python manage.py migrate

5.4 No arquivo posts/views.py

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

5.5 no arquivo posts/urls.py 

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                # Página inicial
    path('lista/', views.lista_jogos, name='lista_jogos'),  # Lista de jogos
    path('jogar/<int:jogo_id>/', views.jogar, name='jogar'), # Jogar um jogo específico
]

5.6 No arquivo blog/urls.py

from django.contrib import admin
from django.urls import path
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
]

5.7 Crie as pastas e os templates

posts/templates/posts jogar.html jogos.html 
posts/templates/ home.html 


7. Rodar o servidor
python manage.py runserver


8. python manage.py createsuperuser

