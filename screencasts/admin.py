"""Admin interface for the screencasts app."""

from django.contrib import admin
from screencasts.models import Screencast


admin.site.register(Screencast)
