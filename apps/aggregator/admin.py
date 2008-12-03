from django.contrib import admin
from roflpimp.apps.aggregator.models import Feed, FeedItem

admin.site.register(Feed, 
    list_display  = ["title", "public_url", "is_defunct"],
    list_filter   = ["is_defunct"],
    ordering      = ["title"],
    search_fields = ["title", "public_url"],
    list_per_page = 500,
)

admin.site.register(FeedItem, 
    list_display   = ['title', 'feed', 'date_modified'],
    list_filter    = ['feed'],
    search_fields  = ['feed__title', 'feed__public_url', 'title'],
    date_heirarchy = ['date_modified'],
)