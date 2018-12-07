from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Soundtrack

def index(request):
    Soundtrack = Soundtrack.objects.order_by('soundtrackid')[:5]
    template = loader.get_template('soundtrackList/index.html')
    context = {
        'Soundtrack': Soundtrack,
    }
    return HttpResponse(template.render(context, request))