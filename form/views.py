from django.shortcuts import render, redirect
from .form import UserForm
from . import Controller

# Create your views here.
def index(request):
    form = UserForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():

            user_keyword = form['keyword'].value()
            start_date = form['startdate'].value()
            end_date = form['enddate'].value()
            twitter = form['twitter'].value()
            reddit = form['reddit'].value()

            search = Controller.SearchParam(start_date, end_date, user_keyword, twitter, reddit)
            search.runSearch()

            return redirect('wordcloud')
            #pass
        #else:
            #print(form['keyword'].value())
            #print(form.errors)
            #form = UserForm()
    return render(request, "index.html", {'form': form, 'errors': form.errors})

def datavis(request):
    return render(request, "datavis.html")

def wordcloud(request):
    return render(request, "wordcloud.html")

def locationcloud(request):
    return render(request, "locationcloud.html")
