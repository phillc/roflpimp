from django.views.generic.simple import direct_to_template
from roflpimp.apps.aggregator.models import Feed

def home(request):
    feeds = list(Feed.objects.all())
    if True:#not request.user or request.user.position_set:
        num_feeds = len(feeds)
        #attempting to evenly distribute feeds across column initially
        num_in_columns = num_feeds // 3
        extra = num_feeds % 3
        if extra == 1:
            extra_first = 1
            extra_second = 0
        elif extra == 2:
            extra_first = 1
            extra_second = 1
        else:
            extra_first = 0
            extra_second = 0
            
        end_first = num_in_columns + extra_first
        first_column = feeds[0:end_first]
        end_second = end_first + num_in_columns + extra_second
        second_column = feeds[end_first:end_second]
        third_column = feeds[end_second:]
        
        print num_in_columns
        print extra_first
        print extra_second
        print first_column
        print second_column
        print third_column

    return direct_to_template(request, 'aggregator/home.html', {'first_column': first_column, 'second_column': second_column, 'third_column': third_column})
