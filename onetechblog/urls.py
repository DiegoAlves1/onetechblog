from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^artigo/(?P<pk>[0-9]+)/$', views.artigo_detalhe, name='artigo_detalhe'),
	url(r'^artigo/new/$', views.artigo_new, name='artigo_new'),
	url(r'^artigo/(?P<pk>[0-9]+)/edit/$', views.artigo_edit, name='artigo_edit'),
	url(r'^drafts/$', views.artigo_draft_list, name='artigo_draft_list'),
	url(r'^artigo/(?P<pk>\d+)/publish/$', views.artigo_publish, name='artigo_publish'),
	url(r'^artigo/(?P<pk>\d+)/remove/$', views.artigo_remove, name='artigo_remove'),

]