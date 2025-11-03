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
