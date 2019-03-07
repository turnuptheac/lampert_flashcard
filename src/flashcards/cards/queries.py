from datetime import datetime

from .models import Flashcard

def next_card():
  """Retrieves the next available card for the user to guess."""
  return Flashcard.objects \
    .filter(visible_after__lte=datetime.utcnow(), # show visible cards
            failure_count__lte=9,                 # hide failed cards
            bucket_number__lte=10                 # hide final bucket
    ) \
    .order_by('-bucket_number')[0:1] \
    .get()                                        # return one result

def list_cards(starts_with=""):
  """
  Retrieves a list of up to 100 cards, sorted descending by creation date, 
  and starting with 'starts_with' letters. If no 'starts_with' value is 
  specified, all words return.
  """
  return Flashcard.objects.filter(word__startswith=starts_with) \
                          .order_by('-created_at')[0:100]

def has_pending_cards():
  """Checks if a patient user will have any cards left to guess."""
  return Flashcard.objects \
    .filter(failure_count__lte=9,                 # hide failed cards
            bucket_number__lte=10                 # hide final bucket
    ) \
    .exists()

def has_any_cards():
  """Checks if the user has made any cards."""
  return Flashcard.objects.all().exists()
  
def get_by_id(card_id):
  """Gets a card by its id."""
  return Flashcard.objects.get(pk=card_id)