from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to="profiles/", null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"
    
@receiver(post_save, sender=User)
def criar_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        

class Jogo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    codigo = models.TextField()

    def __str__(self):
        return self.nome
    

class Comentario(models.Model):
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comentário de {self.usuario.username} em {self.jogo.nome}"

class Curtida(models.Model):
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('jogo', 'usuario')  # impede curtir duas vezes

    def __str__(self):
        return f"{self.usuario.username} curtiu {self.jogo.nome}"
    
