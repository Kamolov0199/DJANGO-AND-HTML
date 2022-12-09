from django.shortcuts import render
from .models import Post
from .models import TopPost
from django.views.generic import *





class AboutView(TemplateView):
    template_name = 'about.html'
    
class IndexView(TemplateView):
    template_name = 'index.html'
    
