from django.shortcuts import render
from django.http import HttpResponse
from feed.models import Message

def index(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        user = request.user

        Message.objects.create(content=content, user=user)

    context = {}

    context['messages'] = Message.objects.order_by('-created_at')

    return render(request, 'index.html', context=context)


def details(request, id):
    if request.method == 'POST':
        content = request.POST.get('content')
        user = request.user

        Message.objects.create(content=content, user=user, response_to_id=id)

    context = {}
    context['message'] = Message.objects.get(id=id)
    context['comments'] = Message.objects.filter(response_to=id)

    return render(request, 'details.html', context=context)
