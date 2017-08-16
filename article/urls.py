from django.conf.urls import url,include
from article import views

urlpatterns = [
    url(r'^view1/$',views.Myview),
    url(r'^hello_dunia/$',views.Hello_world),
    url(r'^namaSaya/(?P<nama_saya>[\w-]+)/(?P<umur>[0-9]+)$',views.NamaSaya),
    url(r'^Coba/$',views.Coba),
]