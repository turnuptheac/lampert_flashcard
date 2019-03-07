"""flashcards URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from . import views

app_name = 'cards'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^flashcard$', views.list, name='list'),
    url(r'^flashcard/definition$', views.definition, name='definition'),
    url(r'^flashcard/create$', views.create, name='create'),
    url(r'^flashcard/update/(?P<card_id>.+)$', views.update, name='update'),
    url(r'^flashcard/guess/correct$', views.guess_correctly, name='guess_correctly'),
    url(r'^flashcard/guess/incorrect$', views.guess_incorrectly, name='guess_incorrectly'),
]