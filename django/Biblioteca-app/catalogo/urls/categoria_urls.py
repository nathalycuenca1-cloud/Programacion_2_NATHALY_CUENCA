from django.urls import path
from catalogo.views.categoria_views import categoria_list, categoria_create, categoria_update, categoria_delete

urlpatterns = [
    path('', categoria_list, name='categoria_list'),
    path('nueva/', categoria_create, name='categoria_create'),
    path('<int:pk>/editar/', categoria_update, name='categoria_update'),
    path('<int:pk>/eliminar/', categoria_delete, name='categoria_delete'),
]