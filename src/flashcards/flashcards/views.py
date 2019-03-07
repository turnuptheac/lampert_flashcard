from django.shortcuts import render

def index(request):
  return render(request, 'flashcards/index.html')

def definition(request, flashcard_id):
  return render(request, 'flashcards/definition.html')

def list(request):
  return render(request, 'flashcards/list.html')

def new(request):
  return render(request, 'flashcards/new.html')