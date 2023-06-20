from django.contrib import admin
from django.urls import  include, path


urlpatterns = [
    path('', include ('mundo1real.urls')),
    path('admin/', admin.site.urls),
    path('produtos/', include('cad_produtos.urls')),

]
