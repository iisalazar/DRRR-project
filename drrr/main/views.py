from django.shortcuts import render
from . import models
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
# Create your views here.

class ContentList(generic.ListView):
    model = models.Content
    

class ContentCreate(generic.CreateView):
    model = models.Content
    template_name = ''