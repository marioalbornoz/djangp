from django.conf.urls import url

from apps.mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete, \
    MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete

'''
urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^nuevo$', mascota_view, name="mascota_crear"),
    url(r'^listar$', mascota_list, name="mascota_listar"), #usar en el template el diccionario mascotas
    url(r'^listar/editar/(?P<id_mascota>\d+)/$', mascota_edit, name='mascota_editar'),
    url(r'^listar/eliminar/(?P<id_mascota>\d+)/$', mascota_delete, name='mascota_eliminar'),
]
'''
urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^nuevo$', MascotaCreate.as_view(), name='mascota_crear'),
    url(r'^listar', MascotaList.as_view(), name='mascota_listar'), #cambiar en el template el diccionario mascota por object list
    url(r'^editar/(?P<pk>\d+)/$', MascotaUpdate.as_view(), name='mascota_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$',MascotaDelete.as_view(), name='mascota_eliminar'),
]