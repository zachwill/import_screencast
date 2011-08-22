"""Models for screencasts."""

import re
from urllib import urlencode

from markdown import markdown
from django.db import models
from django.template.defaultfilters import slugify


class Screencast(models.Model):
    """A model for screencasts."""
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=75)
    slug = models.SlugField(blank=True)
    vimeo_url = models.URLField('Vimeo URL', verify_exists=False)
    description_markdown = models.TextField('Markdown Description')
    description = models.TextField('Description', blank=True, null=True)
    vimeo_id = models.CharField('Vimeo ID', max_length=50, blank=True)
    embed_url = models.URLField('Embed URL', verify_exists=False, blank=True)

    def __unicode__(self):
        """Give each Screencast a name."""
        return self.title

    def get_absolute_url(self):
        """Method to get unique URL for a screencast."""
        return '/screencast/%s/' % self.slug

    def create_embed_url(self, vimeo_id):
        """Create an embed URL that can be used with iframe elements."""
        params = urlencode({
            'byline': 0,
            'color': '6b1bdf',
            'portrait': 0,
            'title': 0,
        })
        embed_url = 'http://player.vimeo.com/video/%s?%s' % (vimeo_id, params)
        return embed_url

    def parse_vimeo_id(self, vimeo_url):
        """Parse the unique vimeo ID from the vimeo URL."""
        return re.search(r'\d+', vimeo_url).group()

    def save_slug(self):
        """
        If the screencast does not already have a slug, create one from the
        title.
        """
        if not self.slug:
            self.slug = slugify(self.title)

    def save(self):
        """
        Several of the fields are actually set on save. Normally, only the
        `description_markdown`, `title`, and `vimeo_url` will be introduced
        when initialized.
        """
        vimeo_id = self.parse_vimeo_id(self.vimeo_url)
        self.vimeo_id = vimeo_id
        self.embed_url = self.create_embed_url(vimeo_id)
        self.description = markdown(self.description_markdown)
        self.save_slug()
        super(Screencast, self).save()
