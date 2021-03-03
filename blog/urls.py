from django.conf.urls import include, url
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    url(r'^$', views.post_list, name='inicio'),
    url(r'^post/(?P<id_post>[0-9]+)/$', login_required(views.post_detail) , name='ver_post'),
    url(r'^post/(?P<id_post>[0-9]+)/edit/$', login_required(views.post_edit), name='edit_post'),
    url(r'^post/new/$', login_required(views.post_new), name='post_new'),

    ##el sistema de vista por clase de login y logout viene definido en Djnago
    url(r'^accounts/login',LoginView.as_view(template_name='blog/login.html'), name='login'), #login,usa la plantilla login.html
    #en setting(opcional) se puede configurar LOGIN_REDIRECT_URL para que nos redireccione a un html en particualr 
    ### la ruta acoounts/login, es porque por defecto login_required nos manda
    url(r'^logout$',LogoutView.as_view(template_name='blog/logout.html'), name='logout'), #logout, nos manda a index.html y en setting(opcional) LOGOUT_REDIRECT_URL
]