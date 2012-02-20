import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

try:
    from django.utils.timezone import now
except ImportError:
    now = datetime.datetime.now


class WaitingListEntry(models.Model):
    
    email = models.EmailField(_("email address"), unique=True)
    created = models.DateTimeField(_("created"), default=now, editable=False)
    
    class Meta:
        verbose_name = _("waiting list entry")
        verbose_name_plural = _("waiting list entries")
