from django.urls import include, path
from catalogo.views.categoria_views import home

urlpatterns = [
    path('', home, name='home'),
    path('categorias/', include('catalogo.urls.categoria_urls')),
    path('libros/', include('catalogo.urls.libro_urls')),
]
