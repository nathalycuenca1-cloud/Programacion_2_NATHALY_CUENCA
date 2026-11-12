from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalogo.urls.home_urls')),
    path(
        'catalogo/catalogo/',
        RedirectView.as_view(url='/catalogo/'),
    ),
    path(
        'catalogo/catalogo/libros/<path:remaining>',
        RedirectView.as_view(
            url='/catalogo/libros/%(remaining)s',
            query_string=True,
        ),
    ),
    path(
        'catalogo/catalogo/libros/',
        RedirectView.as_view(url='/catalogo/libros/'),
    ),
    path('catalogo/', include('catalogo.urls')),
    path('catalogo/autor/', include('catalogo.urls.autor_urls')),
    path('cuentas/', include('catalogo.urls.aunthentication_urls')),
]
