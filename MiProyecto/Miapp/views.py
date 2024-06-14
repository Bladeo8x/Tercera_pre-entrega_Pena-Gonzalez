from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Author, Book, Review
from .forms import AuthorForm, BookForm, ReviewForm, SearchForm

def index(request):
    return render(request, 'Miapp/index.html')

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = AuthorForm()
    return render(request, 'Miapp/add_author.html', {'form': form})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = BookForm()
    return render(request, 'Miapp/add_book.html', {'form': form})

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ReviewForm()
    return render(request, 'Miapp/add_review.html', {'form': form})

def search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Book.objects.filter(title__icontains=query)
            return render(request, 'Miapp/search_results.html', {'results': results, 'query': query})
    else:
        form = SearchForm()
    return render(request, 'Miapp/search.html', {'form': form})
