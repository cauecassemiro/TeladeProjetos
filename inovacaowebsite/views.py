from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse
from .models import Equipe, Parceiro, Noticia, Album, Imagem, Contato

def home(request):
  template = loader.get_template('pages/home/home.html')
  context = {
             'equipe': Equipe.objects.all(),
             'parcerias': Parceiro.objects.all(),
             'noticias': Noticia.objects.order_by('-data')[:4]
            }
  return HttpResponse(template.render(context, request))

# Galeria de fotos

def galeria(request):
  template = loader.get_template('pages/galeria/galeria.html')
  context = {'albuns': Album.objects.order_by('-data')}
  return HttpResponse(template.render(context, request))

def album(request, album_id):
  try:
    chosenAlbum = Album.objects.get(id=album_id)
    template = loader.get_template('pages/galeria/galeria2.html')
    context = {'imagens': Imagem.objects.filter(album=chosenAlbum).order_by('-data')}
    return HttpResponse(template.render(context, request))
  except Album.DoesNotExist:
    return redirect('home')

# Contato

def contato(request):
  if(request.method == 'POST'):
    contato = Contato(nome=request.POST['nome'], email=request.POST['email'], mensagem=request.POST['assunto'], assunto=request.POST['mensagem'])
    contato.save()
  template = loader.get_template('pages/contato/contato.html')
  return HttpResponse(template.render({}, request))

# Notícias

def noticias(request):
  template = loader.get_template('pages/noticias/noticias.html')
  context = {'noticias': Noticia.objects.order_by('-data')}
  return HttpResponse(template.render(context, request))

def noticia(request, noticia_id):
  try:
    chosenNoticia = Noticia.objects.get(id=noticia_id)
    template = loader.get_template('pages/noticias/noticia.html')
    context = {'noticia': chosenNoticia,
               'noticias': Noticia.objects.order_by('-data')[:5]}
    return HttpResponse(template.render(context, request))
  except Noticia.DoesNotExist:
    return redirect('home')
  
  # Projetos

def projetos(request):
  template = loader.get_template('pages/projetos/projetos.html')
  context = {}
  return HttpResponse(template.render(context, request))
  
