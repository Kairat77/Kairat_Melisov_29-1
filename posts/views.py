import datetime
from django.shortcuts import HttpResponse,redirect



# Create your views here.


def hello_views(request):
    if request.method == 'GET':
        return HttpResponse('helo, it`s my first view')
    
def goodby_views(request):
    if request.method == 'GET':
        return HttpResponse('Goodby user!')
    

def redirect_to_youtube_views(request):
    if request.method == 'GET':
        return redirect('https://www.youtube.com')
    
def now_date_views(request):
    if request.method == 'GET':
        current_date = datetime.datetime.now().date()
        return HttpResponse(f'Current date: {current_date}')