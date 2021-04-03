from django.shortcuts import render
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic import TemplateView, CreateView, UpdateView


class HomeView(TemplateView):
    template_name = 'core/index.html'




