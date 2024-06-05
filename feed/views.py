from django.shortcuts import render
from feed.models import Message

def index(request):
    context = {}

    context['messages'] = Message.objects.order_by('-created_at')

    return render(request, 'index.html', context=context)