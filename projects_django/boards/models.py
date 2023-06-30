from django.db import models
import datetime

# Create your models here.
class BoardsModel(models.Model):
    # Campos del modelo
    ESTATUS = (('PI', 'Por iniciar'), ('I','Iniciado'), ('T', 'Terminado'))
    titulo = models.CharField(max_length = 200)
    descripcion = models.TextField()
    valor = models.FloatField(blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modificado = models.DateTimeField(auto_now = True)
    estatus = models.CharField(max_length=20, choices=ESTATUS, default='PI')

    class Meta:
        verbose_name = "tablero"
        verbose_name_plural = "tableros"
        ordering = ["-creado"]
        permissions = (("es_miembro_1", "Es miembro con prioridad 1"),) 

    def __str__(self):
        return self.titulo