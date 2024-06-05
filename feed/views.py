from django.shortcuts import render
from feed.models import Message

def index(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        user = request.user

        Message.objects.create(content=content, user=user)

    context = {}

    context['messages'] = Message.objects.order_by('-created_at')

    return render(request, 'index.html', context=context)