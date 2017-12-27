from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    context = {
        'new_item_text': request.POST.get('item_text', '')
    }
    return render(request, 'twitter/index.html', context)
