from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                # Página inicial
    path('lista/', views.lista_jogos, name='lista_jogos'),  # Lista de jogos
    path('jogar/<int:jogo_id>/', views.jogar, name='jogar'), # Jogar um jogo específico
]
