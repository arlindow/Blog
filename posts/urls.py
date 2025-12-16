from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                # Página inicial
    path('lista/', views.lista_jogos, name='lista_jogos'),  # Lista de jogos
    path('lista/jogar/<int:jogo_id>/', views.jogar, name='jogar'), # Jogar um jogo específico
    path('jogo/<int:jogo_id>/', views.detalhes_jogo, name="jogo_detalhes"),
    path('jogo/<int:jogo_id>/curtir/', views.curtir, name="curtir"),
    path('jogo/<int:jogo_id>/comentar/', views.comentar, name="comentar"),
    path('login/', views.login_cadastro_view, name="login"),
]

