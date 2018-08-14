from django.shortcuts import render, redirect
from .form import UserForm
from . import Controller

# Create your views here.
def index(request):
    form = UserForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            search = SearchParam(UserForm.keyword, UserForm.startdate, UserForm.enddate, UserForm.twitter, UserForm.reddit)
            search.runSearch()
            print(form.cleaned_data['keyword'])

            #return redirect('datavis')
            #pass
        else:
            print(form['keyword'].value())
            form = UserForm()
    return render(request, "index.html", {'form': form})

def datavis(request):

    return render(request, "datavis.html")
