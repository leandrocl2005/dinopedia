from django.db import models


# Create your models here.
class Dinosaur(models.Model):

  name = models.CharField('nome', max_length=100, unique=True)
  description = models.TextField('descrição', null=True, blank=True)
  photo = models.ImageField(upload_to='static/img', null=True, blank=True)

  class Meta:
    ordering = ('name', )
    verbose_name = "Dinossauro"
    verbose_name_plural = "Dinossauros"

  def __str__(self):
    return self.name
