from app0.models import Ids
import random


def shuffle():
    val = id=random.randint(a=1001, b=99999999)
    while (Ids.objects.filter(pk=val).exists()):
        val = id=random.randint(a=1001, b=99999999)
    newid = Ids(id=val)
    newid.save()
    return val

