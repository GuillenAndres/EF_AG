from django.urls import path

from AppBuild.views import *


urlpatterns = [
    path('', inicio, name='AppBuildInicio'),
    path('obra_formulario/', obra_formulario, name='AppBuildObraFormulario'),

    path('obrero_formulario/', obrero_formulario, name='AppBuildObreroFormulario'),
    path('arquitecto_formulario/', arquitecto_formulario, name='AppBuildArquitectoFormulario'),
    path('busqueda_tipo/', busqueda_tipo, name= 'AppBuildBusquedaTipo'),
    path('busqueda_tipo_post/', busqueda_tipo_post, name= 'AppBuildBusquedaTipoPost'),

    path('EFinal_AGObra/', obra_formulario, name='AppBuildObra'),

]
