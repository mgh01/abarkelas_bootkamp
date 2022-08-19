from django.shortcuts import render
from django.views.generic import TemplateView


class WorkInfo(TemplateView):
    template_name = "workInfo.html"
