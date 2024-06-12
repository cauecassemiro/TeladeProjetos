from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [path('', home, name='home'),
               path('galeria', galeria, name='galeria'),
               path('galeria/album/<int:album_id>', album, name='album'),
               path('contato', contato, name='contato'),
               path('noticias', noticias, name='noticias'),
               path('projetos', projetos, name='projetos'),]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)