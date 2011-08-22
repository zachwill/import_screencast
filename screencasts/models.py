"""Models for screencasts."""

import re
from urllib import urlencode

from markdown import markdown
from django.db import models
from django.template.defaultfilters import slugify


class Screencast(models.Model):
    """A model for screencasts."""
    title = models.CharField('Title', max_length=75)
    slug = models.SlugField()
    description_markdown = models.TextField('Markdown Description')
    description = models.TextField('Description', blank=True, null=True)
    vimeo_id = models.CharField(max_length=50, unique=True)
    vimeo_url = models.URLField('Vimeo URL', verify_exists=False)
    embed_url = models.URLField(verify_exists=False)

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
        self.slug = slugify(self.title)
        super(Screencast, self).save()
