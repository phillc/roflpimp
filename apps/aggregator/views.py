from django.views.generic.simple import direct_to_template
from roflpimp.apps.aggregator.models import Feed

def home(request):
    #list called to prevent multiple calls when sliced
    feeds = list(Feed.objects.all())
    if True:#not request.user or request.user.position_set:
        #distribute feeds evenely to columns initially
        first_column = feeds[::3]
        second_column = feeds[1::3]
        third_column = feeds[2::3]
        
    return direct_to_template(request, 'aggregator/home.html', {'first_column': first_column, 'second_column': second_column, 'third_column': third_column})
