from unicodedata import category

from django.shortcuts import render
from .models import *
from django.views import generic


class HomeView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()[0]
        context['products'] = Product.objects.filter(category=context['category'])
        return context


class ProductListView(generic.ListView):
    queryset = Product.objects.all()
    template_name = 'catalog.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



class RegisterView(generic.TemplateView):
    template_name = 'register.html'


class LoginView(generic.TemplateView):
    template_name = 'login.html'
