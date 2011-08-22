"""Feeds for the latest screencasts."""

from django.contrib.syndication.views import Feed
from screencasts.models import Screencast


class LatestScreencasts(Feed):
    """A feed for the latest screencasts."""
    title = 'importscreencast.com'
    link = '/'
    description = 'New and updated screencasts.'

    def items(self):
        return Screencast.objects.order_by('-date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description
