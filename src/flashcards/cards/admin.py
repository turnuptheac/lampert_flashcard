from django.contrib import admin
from .models import Flashcard

# Register your models here.
def guess_incorrectly(modeladmin, request, queryset):
    for card in queryset:
      card.add_failure()
      card.save()
guess_incorrectly.short_description = "I didn't get it."

def guess_correctly(modeladmin, request, queryset):
  for card in queryset:
    card.increment_bucket()
    card.save()
guess_correctly.short_description = "I got it."

class FlashcardAdmin(admin.ModelAdmin):
  fields = ('word', 'definition', 'bucket_number', 'failure_count', 'visible_after')

  date_hierarchy = 'created_at'

  actions = [guess_correctly, guess_incorrectly]

admin.site.register(Flashcard, FlashcardAdmin)