from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'hotels/hotels.html')

def hotels(request):
    return render(request, 'hotels/hotel.html')

def search(request):
    return render(request, 'hotels/search.html')