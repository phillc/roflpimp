from django.contrib.syndication.feeds import Feed
from roflpimp.apps.aggregator.models import FeedItem

class CommunityAggregatorFeed(Feed):
    title = "The rofl pimp aggregator"
    link = "/all/"
    description = "Aggregated feeds for rofl."

    def items(self):
        return FeedItem.objects.all()[:10]