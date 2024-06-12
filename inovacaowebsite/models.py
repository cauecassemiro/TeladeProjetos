from django.db import models
import datetime

class Noticia(models.Model):
    imagem = models.ImageField(upload_to='noticias')
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    conteudo = models.TextField()
    autor = models.CharField(max_length=100, default='Inovação JFPB')
    slug = models.SlugField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Equipe(models.Model):
    imagem = models.ImageField(upload_to='equipe')
    nome = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    funcao = models.CharField(max_length=100)
    twitter = models.URLField(max_length=200, blank=True)
    facebook = models.URLField(max_length=200, blank=True)
    instagram = models.URLField(max_length=200, blank=True)
    linkedin = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.nome
    
class Parceiro(models.Model):
    imagem = models.ImageField(upload_to='parceiros')
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.nome
    
# Galeria de imagens

class Album(models.Model):
    capa = models.ImageField(upload_to='galeria')
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Albuns"
        ordering = ['-data']

    def __str__(self):
        return self.titulo
    
class Imagem(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='galeria')
    descricao = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Imagens"
        ordering = ['-data']

    def __str__(self):
        return self.descricao
    
# Contato
class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    assunto = models.CharField(max_length=100)
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data']

    def __str__(self):
        return self.nome + ' - ' + self.assunto
