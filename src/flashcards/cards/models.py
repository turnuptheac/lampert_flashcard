from django.db import models
from datetime import datetime, timedelta

BUCKETS = [
  timedelta(seconds=0),    # bin 0
  timedelta(seconds=5),    # bin 1
  timedelta(seconds=25),   # bin 2
  timedelta(minutes=2),    # bin 3
  timedelta(minutes=10),   # bin 4
  timedelta(hours=1),      # bin 5
  timedelta(hours=5),      # bin 6
  timedelta(days=1),       # bin 7
  timedelta(days=5),       # bin 8
  timedelta(days=25),      # bin 9
  timedelta(days=30*4),    # bin 10 - approximately four months
  timedelta(days=365*300), # bin 11 - impure, but pragmatic
]

class Flashcard(models.Model):
  word = models.CharField(max_length=100, blank=False)
  definition = models.TextField(max_length=500, blank=False)
  bucket_number = models.IntegerField(default=0, blank=False)
  visible_after = models.DateTimeField()
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