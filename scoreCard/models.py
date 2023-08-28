from django.db import models
from django.contrib.auth.models import User


class Golfer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    do_dodge = models.IntegerField(default=0)
    elbow_room = models.IntegerField(default=0)
    wigwam = models.IntegerField(default=0)
    depot = models.IntegerField(default=0)
    sports_page = models.IntegerField(default=0)
    reboot = models.IntegerField(default=0)
    mouse_trap = models.IntegerField(default=0)
    clancys = models.IntegerField(default=0)
    dooleys = models.IntegerField(default=0)
    gi = models.IntegerField(default=0)
    brothers = models.IntegerField(default=0)
    pio = models.IntegerField(default=0)
    pickle = models.IntegerField(default=0)
    shenanns = models.IntegerField(default=0)
    brat = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

    def __str__(self):
        if self.user is None:
            return "no_name"
        else:
            return self.user.username


class BarPar(models.Model):
    do_dodge = models.IntegerField(default=0)
    elbow_room = models.IntegerField(default=0)
    wigwam = models.IntegerField(default=0)
    depot = models.IntegerField(default=0)
    sports_page = models.IntegerField(default=0)
    reboot = models.IntegerField(default=0)
    mouse_trap = models.IntegerField(default=0)
    clancys = models.IntegerField(default=0)
    dooleys = models.IntegerField(default=0)
    gi = models.IntegerField(default=0)
    brothers = models.IntegerField(default=0)
    pio = models.IntegerField(default=0)
    pickle = models.IntegerField(default=0)
    shenanns = models.IntegerField(default=0)
    brat = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

    def __str__(self):
        return "Bar Par"
