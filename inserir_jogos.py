import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
django.setup()

from posts.models import Jogo

jogos = [
    {
        "nome": "🐍 Jogo da Cobrinha (Snake Game)",
        "descricao": "Controle a cobrinha, coma a fruta e evite bater nas paredes.",
        "codigo": """<canvas id='snake' width='400' height='400'></canvas>
<script>
const canvas=document.getElementById('snake'),ctx=canvas.getContext('2d');
let box=20,snake=[{x:9*box,y:10*box}],dir='RIGHT';
let food={x:Math.floor(Math.random()*19+1)*box,y:Math.floor(Math.random()*19+1)*box};
document.addEventListener('keydown',e=>{
 if(e.keyCode==37&&dir!='RIGHT')dir='LEFT';
 if(e.keyCode==38&&dir!='DOWN')dir='UP';
 if(e.keyCode==39&&dir!='LEFT')dir='RIGHT';
 if(e.keyCode==40&&dir!='UP')dir='DOWN';
});
function draw(){
 ctx.fillStyle='#111';ctx.fillRect(0,0,400,400);
 snake.forEach((s,i)=>{ctx.fillStyle=i?'#fff':'#0f0';ctx.fillRect(s.x,s.y,box,box);});
 ctx.fillStyle='#f00';ctx.fillRect(food.x,food.y,box,box);
 let h={...snake[0]};
 if(dir=='LEFT')h.x-=box;if(dir=='RIGHT')h.x+=box;
 if(dir=='UP')h.y-=box;if(dir=='DOWN')h.y+=box;
 if(h.x==food.x&&h.y==food.y)
  food={x:Math.floor(Math.random()*19+1)*box,y:Math.floor(Math.random()*19+1)*box};
 else snake.pop();
 if(h.x<0||h.y<0||h.x>=400||h.y>=400)clearInterval(game);
 snake.unshift(h);
}
let game=setInterval(draw,100);
</script>"""
    },
    {
        "nome": "🧠 Jogo da Memória",
        "descricao": "Combine os pares de emojis no menor tempo possível.",
        "codigo": """<div id='tab'></div>
<script>
const emojis=['😀','😀','🐍','🐍','🎮','🎮','👾','👾'];
let sel=[],tab=document.getElementById('tab');
tab.style.display='grid';tab.style.gridTemplateColumns='repeat(4,60px)';
tab.style.gap='10px';
emojis.sort(()=>0.5-Math.random()).forEach(e=>{
 let b=document.createElement('button');
 b.textContent='?';b.style.fontSize='24px';
 b.onclick=()=>{
  if(sel.length<2&&b.textContent=='?'){
   b.textContent=e;sel.push(b);
   if(sel.length==2){
    if(sel[0].textContent!=sel[1].textContent)
     setTimeout(()=>sel.forEach(x=>x.textContent='?'),700);
    sel=[];
   }
  }
 };
 tab.appendChild(b);
});
</script>"""
    },
    {
        "nome": "🏓 Pong Clássico",
        "descricao": "Derrote a IA no clássico Pong.",
        "codigo": """<canvas id='pong' width='400' height='300'></canvas>
<script>
const c=document.getElementById('pong'),x=c.getContext('2d');
let p={y:120},a={y:120},b={x:200,y:150,dx:3,dy:3};
c.onmousemove=e=>p.y=e.offsetY-40;
function d(){
 x.fillStyle='#000';x.fillRect(0,0,400,300);
 x.fillStyle='#0f0';x.fillRect(10,p.y,10,80);
 x.fillRect(380,a.y,10,80);
 x.beginPath();x.arc(b.x,b.y,8,0,7);x.fill();
 b.x+=b.dx;b.y+=b.dy;
 if(b.y<0||b.y>300)b.dy*=-1;
 if(b.x<20||b.x>380)b.dx*=-1;
 a.y=b.y-40;
}
setInterval(d,30);
</script>"""
    },
    {
        "nome": "❌⭕ Jogo da Velha",
        "descricao": "Clássico jogo da velha para dois jogadores.",
        "codigo": """<div id='jv'></div>
<script>
let c='',d=document.getElementById('jv');
d.style.display='grid';d.style.gridTemplateColumns='repeat(3,80px)';
for(let i=0;i<9;i++){
 let b=document.createElement('button');
 b.style.height='80px';b.style.fontSize='30px';
 b.onclick=()=>{if(!b.textContent){b.textContent=c=c=='X'?'O':'X';}};
 d.appendChild(b);
}
</script>"""
    },
    {
        "nome": "🎯 Jogo de Clique Rápido",
        "descricao": "Clique no botão o máximo que conseguir em 5 segundos.",
        "codigo": """<button id='btn'>Clique!</button><p id='r'>0</p>
<script>
let n=0,t=false;
btn.onclick=()=>{
 if(!t){t=true;setTimeout(()=>alert('Pontuação: '+n),5000);}
 n++;r.textContent=n;
};
</script>"""
    },
    {
        "nome": "🧮 Jogo de Matemática",
        "descricao": "Resolva operações matemáticas simples.",
        "codigo": """<p id='q'></p><input id='a'><button>OK</button>
<script>
let x=Math.floor(Math.random()*10),y=Math.floor(Math.random()*10);
q.textContent=`${x} + ${y} = ?`;
document.querySelector('button').onclick=()=>{
 alert(a.value==x+y?'Correto!':'Errado!');
};
</script>"""
    },
    {
        "nome": "🏎️ Jogo de Desvio",
        "descricao": "Desvie dos obstáculos o máximo que puder.",
        "codigo": """<canvas id='race' width='300' height='300'></canvas>
<script>
const c=document.getElementById('race'),x=c.getContext('2d');
let p=150,o=0;
document.onmousemove=e=>p=e.offsetX;
function g(){
 x.clearRect(0,0,300,300);
 x.fillRect(p-15,260,30,30);
 x.fillRect(o,0,20,20);
 o+=2;if(o>300)o=Math.random()*280;
}
setInterval(g,30);
</script>"""
    },
    {
        "nome": "🔢 Jogo de Adivinhação",
        "descricao": "Tente adivinhar o número secreto.",
        "codigo": """<input id='n'><button>Enviar</button>
<script>
let s=Math.floor(Math.random()*10);
document.querySelector('button').onclick=()=>{
 alert(n.value==s?'Acertou!':'Tente novamente');
};
</script>"""
    }
]

for jogo in jogos:
    obj, created = Jogo.objects.get_or_create(
        nome=jogo["nome"],
        defaults={
            "descricao": jogo["descricao"],
            "codigo": jogo["codigo"]
        }
    )
    print("✅ Criado:" if created else "⚠️ Já existe:", jogo["nome"])

print("🎮 Jogos carregados com sucesso!")
