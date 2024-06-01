from datetime import datetime
from django.shortcuts import render

def index(request):
    context = {
        'messages': [
            {
                'content': 'text',
                'username': 'CommentCoder',
                'created_at': datetime.now()
            }
        ]
    }

    return render(request, 'index.html', context=context)