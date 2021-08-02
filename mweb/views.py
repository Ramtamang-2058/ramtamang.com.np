from django.shortcuts import render, redirect
from mweb.forms import *
# Create your views here.
def main(request):
    teams = OurTeam.objects.all()
    teams2 = OurTeam2.objects.all()
    form = ContactForm()
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main') 
    context = {'form':form, 'teams': teams, 'teams2': teams2}
    return render(request, 'mweb/index.html', context)

def about(request):
    return render(request, 'mweb/about.html')

def contact(request):
    form = ContactForm()
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main') 
    context = {'form':form}
    return render(request, 'mweb/contact.html', context)

def rate(request):
    return render(request, 'mweb/rate.html')

def portfolio(request):
    projects = Portfolio.objects.all()
    cs = Certificate.objects.all()
    context = {'projects': projects, 'cs': cs}
    return render(request, 'mweb/portfolio.html', context)

def viewMovie(request, pk):
    projects = Portfolio.objects.get(id=pk)
    reviews = Review.objects.filter(project = projects)
    features = Features.objects.filter(project = projects)
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.project = projects
            rate.save()
            return render(request, 'mweb/Mview.html')
    else:
        form = RateForm()

    context = {'projects':projects, 'form': form, 'reviews': reviews, 'features':features,}
    return render(request, 'mweb/Mview.html', context)

def blog(request):
    blogs = Blog.objects.all()
    posts = Recent.objects.all()
    context = {'blogs': blogs, 'posts': posts}
    return render(request, 'mweb/myblog.html', context)

def Hire(request):
    return render(request, 'mweb/hire.html')