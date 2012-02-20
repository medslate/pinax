import datetime

from pinax.apps.waitinglist.models import WaitingListEntry

try:
    from django.utils.timezone import now
except ImportError:
    now = datetime.datetime.now


def stats():
    return {
        "waiting_list_entries": WaitingListEntry.objects.count(),
        
        "waitinglist_added_last_seven_days": WaitingListEntry.objects.filter(created__gt=now() - datetime.timedelta(days=7)).count(),
        "waitinglist_added_last_thirty_days": WaitingListEntry.objects.filter(created__gt=now() - datetime.timedelta(days=30)).count(),
    }
