"""django_init URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aplicaciones.principal.views import inicio,crear_persona,editar_persona,eliminarPersona
from django.config.urls.static import static
from django.config import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='index'),
    path('nuevapersona/', crear_persona, name='nuevapersona'),
    path('editarpersona/<int:id>/', editar_persona, name='editarpersona'),
    path('eliminarpersona/<int:id>/',eliminarPersona, name='eliminarpersona')
] +static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)