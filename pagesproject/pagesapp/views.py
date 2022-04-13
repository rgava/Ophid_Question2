from django.shortcuts import render
from django.views.generic import ListView, DetailView,TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from .models import PagesModel

# Create your views here.
class HomePageView(TemplateView):
    model=PagesModel
    template_name='home.html'

class HomeDetailView(DetailView):
    model=PagesModel
    template_name='detail.html'

class TheListView(ListView):
    model=PagesModel
    template_name='thelist.html'

class NewView(CreateView):
    model=PagesModel
    template_name='new.html'
    fields='__all__'
    
class HomeUpdateView(UpdateView):
    model=PagesModel
    template_name='update.html'
    fields=('name','is_this_male','body',)

class DeleteUpdateView(DeleteView):
    model=PagesModel
    template_name='delete.html'
    success_url = reverse_lazy('thelist')