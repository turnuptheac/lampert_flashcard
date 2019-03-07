FROM python:3.5

ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD src/flashcards/requirements.txt /app/
RUN pip install -r requirements.txt
ADD src/flashcards/ /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]