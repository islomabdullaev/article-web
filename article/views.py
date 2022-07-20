from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import News

class HomePageTemplateView(ListView):
    model = News
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.all()[:4]
        context['latest_stories'] = News.objects.all()[:5]
        context['top_stories'] = News.objects.all()[:2]
        context['top_story'] = News.objects.filter(is_top=True).last()
        return context


class CurrentAffairsTemplateView(TemplateView):
    template_name = "current.html"
