from django.shortcuts import render
from django.http import HttpResponseRedirect
from .form import UserForm

# Create your views here.
def index(request):
    form = UserForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():

            pass
        else:
            form = UserForm()
    return render(request, "index.html", {'form': form})

def datavis(request):
    return render(request, "datavis.html")
