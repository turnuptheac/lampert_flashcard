from datetime import datetime

from .models import Flashcard
from . import queries

def next_card():
  """Retrieves the next available card for the user to guess."""
  try:
    card = queries.next_card()
    has_pending_cards = True
    has_any_cards = True
  except Flashcard.DoesNotExist:
    card = False
    has_pending_cards = queries.has_pending_cards()
    if has_pending_cards == False:
      has_any_cards = queries.has_any_cards()
    else:
      has_any_cards = False
  
  return {
    'card': card,
    'has_pending_cards': has_pending_cards,
    'has_any_cards': has_any_cards
  }

def list_cards(starts_with=""):
  """Retrieves a list of up to 100 cards, sorted descending by creation date, 
     and starting with 'starts_with' letters. If no 'starts_with' value is 
     specified, all words return."""
  return queries.list_cards(starts_with)

def create_card(card):
  """Creates and persists a new card."""
  card.save()

def update_card(card):
  """Updates the persisted value a card."""
  card.save()

def get_card(card_id):
  """Retrieves a card by its ID."""
  return queries.get_by_id(card_id)

def guess_definition_correctly():
  """Correctly guesses the definition of the next available card."""
  card = queries.next_card()
  card.increment_bucket()
  card.save()

def guess_definition_incorrectly():
  """Incorrectly guesses the definition of the next available card."""
  card = queries.next_card()
  card.add_failure()
  card.save()