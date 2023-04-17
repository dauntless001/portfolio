from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class AboutMe(TemplateView):
    template_name = 'about.html'


class ContactMe(TemplateView):
    template_name = 'contact.html'