from django.views.generic.simple import direct_to_template
from roflpimp.apps.aggregator.models import Feed

from django.http import HttpResponse

def home(request):
    
    if request.session.get('first', False) or request.session.get('second', False) or request.session.get('third', False):
        first_column = Feed.objects.filter(id__in=request.session.get('first', False))
        second_column = Feed.objects.filter(id__in=request.session.get('second', False))
        third_column = Feed.objects.filter(id__in=request.session.get('third', False))
    else:
        #list called to prevent multiple calls when sliced
        feeds = list(Feed.objects.all())
        #distribute feeds evenely to columns initially
        first_column = feeds[::3]
        second_column = feeds[1::3]
        third_column = feeds[2::3]
        
    return direct_to_template(request, 'aggregator/home.html', {'first_column': first_column, 'second_column': second_column, 'third_column': third_column})



def update_user(request):
    if request.method == "POST":
        request.session['first'] = request.POST.getlist('first')
        request.session['second'] = request.POST.getlist('second')
        request.session['third'] = request.POST.getlist('third')
        return HttpResponse('ok')
    else:
        return HttpResponse('post only')