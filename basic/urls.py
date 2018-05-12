from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login_user, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^home/$', views.home, name='home'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^posts/$', views.create_post, name='create_post'),
    url(r'^delete/posts/(?P<blog_id>[0-9]+)$', views.delete_post, name='delete_post')
    ]