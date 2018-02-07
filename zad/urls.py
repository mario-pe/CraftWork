from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin



app_name = 'zad'

urlpatterns = [
    # index /zad
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.home, name='home'),

    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'zad/logged_out.html'}, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', views.signup, name='signup'),

    url(r'^add_file/$', views.AddFile.as_view(), name='add_file'),
    url(r'^action_file/(?P<id>\d+)/$', views.ActionFile.as_view(), name='action_file'),
    url(r'^add_url/$', views.AddUrl.as_view(), name='add_url'),
    url(r'^action_url/(?P<id>\d+)/$', views.ActionUrl.as_view(), name='action_url'),

    url(r'^details_url/(?P<id>\d+)/$', views.ActionUrl.as_view(), name='customer_url_details'),
    url(r'^details_file/(?P<id>\d+)/$', views.ActionFile.as_view(), name='customer_file_details'),


    url(r'^upload_info/(?P<id>.+)/$', views.upload_info, name='upload_info'),                    #poprawic i zrobic poludzku
    url(r'^upload_info_file/(?P<id>.+)/$', views.upload_info_file, name='upload_info_file'),
]

