from django.conf.urls import url,include
from article import views

urlpatterns = [
    url(r'^view1/$',views.Myview),
    url(r'^hello_dunia/$',views.Hello_world),
    url(r'^namaSaya/(?P<nama_saya>[\w-]+)/(?P<umur>[0-9]+)$',views.NamaSaya),
    url(r'^Coba/$',views.Coba),
    url(r'^category/(?P<id>[0-9]+)$',views.category_detail),
    url(r'^category/$',views.category_list),
    url(r'^(?P<slug>[\w-]+)$',views.post_detail),

]