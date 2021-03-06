from celery import shared_task
from .models import CorpStat


@shared_task
def update_corpstats(pk):
    cs = CorpStat.objects.get(pk=pk)
    cs.update()


@shared_task
def update_all_corpstats():
    for cs in CorpStat.objects.all():
        update_corpstats.delay(cs.pk)
