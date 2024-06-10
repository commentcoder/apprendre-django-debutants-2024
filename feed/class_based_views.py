from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from feed.models import Message


class MessageListView(ListView):
    model = Message
    context_object_name = 'messages'
    ordering = '-created_at'

    def post(self, request):
        content = request.POST.get('content')
        user = request.user

        message = Message.objects.create(content=content, user=user)

        return redirect('details', id=message.id)


class MessageDetailView(DetailView):
    model = Message

    def post(self, request, pk):
        content = request.POST.get('content')
        user = request.user

        message = Message.objects.create(content=content, user=user, response_to=Message.objects.get(pk=pk))

        return redirect('details', pk=message.id)