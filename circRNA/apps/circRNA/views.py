from django.shortcuts import render

from circRNA.apps.circRNA.models import circRNA

def home(request):
    """ """
    return render(request, 'home.html')

def list(request):
    """ """
    circRNAs = circRNA.objects.all()
    return render(request, 'list.html', {'circRNAs':circRNAs})
