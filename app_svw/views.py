from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView

# Create your views here.

class HomeView(TemplateView):
	template_name = "app_svw/home.html"

class ProductListView(ListView):
	template_name = "app_svw/products.html"
	model = Products


