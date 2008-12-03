from django.db import models

class Feed(models.Model):
    title = models.CharField(max_length=500)
    feed_url = models.URLField(unique=True, max_length=500)
    public_url = models.URLField(max_length=500)
    is_defunct = models.BooleanField()

    def __unicode__(self):
        return self.title

class FeedItemManager(models.Manager):
    def first_five(self):
        return self.all()[:5]

class FeedItem(models.Model):
    feed = models.ForeignKey(Feed)
    title = models.CharField(max_length=500)
    link = models.URLField(max_length=500)
    summary = models.TextField(blank=True)
    date_modified = models.DateTimeField()
    guid = models.CharField(max_length=500, unique=True, db_index=True)

    objects = FeedItemManager()

    class Meta:
        ordering = ("-date_modified",)

    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return self.link
