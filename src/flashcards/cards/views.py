from django.shortcuts import render, redirect
from django.urls import reverse

from .actions import next_card, \
                     list_cards, \
                     guess_definition_correctly, \
                     guess_definition_incorrectly, \
                     create_card, \
                     update_card, \
                     get_card
from .forms import FlashcardForm
from .models import Flashcard

def index(request):
  return render(request, 'cards/index.html', next_card())

def definition(request):
  return render(request, 'cards/definition.html', next_card())

def list(request):
  starts_with = request.GET.get('q', '')
  cards = list_cards(starts_with)

  return render(request, 'cards/list.html', {
    'should_show_search': starts_with == '' and len(cards) > 0, 
    'create_form': FlashcardForm(), 
    'starts_with': starts_with, 
    'results': [{
      'form': FlashcardForm(instance=card),
      'card': card
    } for card in cards]
  })

def guess_correctly(request):
  if request.method == 'POST':
    guess_definition_correctly()
  return redirect(reverse('cards:index'))

def guess_incorrectly(request):
  if request.method == 'POST':
    guess_definition_incorrectly()
  return redirect(reverse('cards:index'))

def create(request):
  if request.method == 'POST':
    form = FlashcardForm(request.POST)
    new_card = form.save(commit=False)
    create_card(new_card)

    if form.is_valid():
      return redirect(reverse('cards:list'))
  return render(request, 'cards/new.html')

def update(request, card_id):
  if request.method == 'POST':
    card = get_card(card_id)
    form = FlashcardForm(request.POST, instance=card)
    card = form.save(commit=False)
    update_card(card)

    if form.is_valid():
      return redirect(reverse('cards:list'))
  return render(request, 'cards/new.html')