from django.http import HttpResponse
from django.shortcuts import render

from django_forms.forms import LegsForm


def index(request):
    return HttpResponse("Hello, world. You're at the django_forms index.")


def triangle(request):

    hyp = None

    if request.method == 'POST':

        form = LegsForm(request.POST)

        if form.is_valid():
            hyp = (int(form.cleaned_data['leg_a'])**2 + int(form.cleaned_data['leg_b'])**2)**0.5
    else:
        form = LegsForm()

    return render(request, 'django_forms/triangle.html', {'form': form, 'hyp': hyp})
