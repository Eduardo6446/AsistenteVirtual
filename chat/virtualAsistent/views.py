from django.shortcuts import render
from .models import Message
import spacy
from datetime import datetime


nlp = spacy.load("en_core_web_sm")

def generate_response(user_input):
    doc = nlp(user_input)
    # Logica basica para respuestas, esto puede ser tan complejo como necesites
    if any(token.text.lower() in ["hello", "hi"] for token in doc):
        return "Hello! How can I help you today?"
    elif "time" in user_input.lower():
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."
    else:
        return "I'm sorry, I don't understand that yet."

def index(request):
    if request.method == "POST":
        user_input = request.POST.get("user_input")
        bot_response = generate_response(user_input)
        message = Message.objects.create(user_input=user_input, bot_response=bot_response)
    else:
        message = None
    
    return render(request, 'assistant/index.html', {'message': message})
