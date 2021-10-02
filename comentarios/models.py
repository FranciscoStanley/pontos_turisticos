from django.db import models

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    data = models.DateTimeField(auto_now=True)
    aprovado = models.BooleanField(default=True)

    def __str__(self):
        return self.usuario.first_name
