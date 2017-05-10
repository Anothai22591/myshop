from django.conf.urls import url

from . import views

app_name = 'shop'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^save_user/$', views.save_user, name='save_user'),
    url(r'^check_user/$', views.check_user_login, name='check_user_login'),
    url(r'^(?P<u_text>[A-Za-z0-9_.]+)/select_item/$', views.select_item, name='select_item'),
    url(r'^clear_order/$', views.clear_order, name='clear_order'),
    url(r'^about/$', views.about, name='about'),

]
