# assistant/views.py

from django.shortcuts import render
from django.http import HttpResponse
from .models import Message
import spacy
from datetime import datetime

nlp = spacy.load("en_core_web_sm")

def generate_response(user_input):
    doc = nlp(user_input)
    if "option1" in user_input.lower():
        return f"que onda"
    elif "option2" in user_input.lower():
        return f"fecha: {datetime.now()}"
    else:
        return "I'm sorry, I don't understand that yet."

def index(request):
    if request.method == "POST":
        user_input = request.POST.get("user_input")
        # Procesar los datos específicos según el valor del botón

        response = generate_response(user_input)
        message = Message.objects.create(user_input=user_input, bot_response=response)
    else:
        message = None

    return render(request, 'assistant/index.html', {'message': message})
