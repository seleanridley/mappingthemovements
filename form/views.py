from django.shortcuts import render
from .form import UserForm

from . import Controller

# Create your views here.
def index(request):
    form = UserForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            ##search = SearchParam(UserForm.keyword, UserForm.startdate, UserForm.enddate, UserForm.twitter, UserForm.reddit)
            ##search.runSearch()
            pass
        else:
            form = UserForm()
    return render(request, "index.html", {'form': form})
