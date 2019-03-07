from django.db import models
from datetime import datetime, timedelta

BUCKETS = [
  timedelta(seconds=0),
  timedelta(seconds=5),
  timedelta(seconds=25),
  timedelta(minutes=2),
  timedelta(minutes=10),
  timedelta(hours=1),
  timedelta(hours=5),
  timedelta(days=1),
  timedelta(days=5),
  timedelta(days=25),
  timedelta(days=30*4),      # approximately four months
  timedelta(days=365*300), # impure, but pragmatic
]

class Flashcard(models.Model):
  word = models.CharField(max_length=100, blank=False)
  definition = models.TextField(max_length=500, blank=False)
  bucket_number = models.IntegerField(default=0, blank=False)
  visible_after = models.TimeField(auto_now_add=True)
  created_at = models.DateField(auto_now_add=True)
  failure_count = models.IntegerField(default=0, blank=False)

  def add_failure(self):
    self.failure_count = self.failure_count + 1
    self.bucket_number = 1
    self.__reset_bucket_timer()
  
  def increment_bucket(self):
    self.bucket_number = self.bucket_number + 1
    self.__reset_bucket_timer()
  
  def __reset_bucket_timer(self):
    self.visible_after = datetime.utcnow() + BUCKETS[self.bucket_number]

  def __str__(self):
    return '%s: %s' % (self.word, self.definition)