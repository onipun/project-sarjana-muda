from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    # if request.method == 'POST': 
    #    return HttpResponse(request.POST['item_text'])

    return render(request, 'home.html', {
        # get -> returing 'item_text' if no, return default which is second argm
        'new_item_text': request.POST.get('item_text',''),
    })