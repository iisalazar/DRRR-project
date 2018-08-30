from django.views import generic
from django.shortcuts import render


#def home(request):
#    return render(request, 'drrr/main.html')

class HomeView(generic.TemplateView):
    template_name = 'drrr/main.html'