from django.conf.urls import url
from app_svw.views import *
from . import views

app_name = ''
urlpatterns = [
	url(r'^$', HomeView.as_view()),
	url(r'^$', ProductListView.as_view(),
]
