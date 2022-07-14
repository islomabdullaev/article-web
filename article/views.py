from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageTemplateView(TemplateView):
    template_name = "index.html"


class CurrentAffairsTemplateView(TemplateView):
    template_name = "current.html"
