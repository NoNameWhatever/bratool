from django.db import models
from django.conf import settings
from simple_history.models import HistoricalRecords
from django.utils.translation import ugettext_lazy as _
import uuid

class Tool(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Name"), max_length=70)
    identification = models.CharField(_("Identification"), max_length=50, blank=True, null=True)
    description = models.TextField(_("Description"), blank=True, null=True)
    keeper = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("keeper"), blank=True, null=True, on_delete=models.SET_NULL)
    department = models.ManyToManyField("bratool.Department", verbose_name=_("department"), null=True, blank=True)
    genre = models.ManyToManyField("tools.Genre", verbose_name=_("genre"), null=True, blank=True)
    models.ImageField(_("Image"), upload_to='tools/%Y/%m/%d/', blank=True, null=True)
    isActive = models.BooleanField(_("active"), default=True)
    history = HistoricalRecords()

    def __str__(self):
        """returning a string representation of Tool"""
        return self.name

class Genre(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Name"), max_length=70)    
    description = models.TextField(_("Description"), blank=True, null=True)    
    departments = models.ManyToManyField("bratool.Department", verbose_name=_("department"), blank=True, null=True)
    isActive = models.BooleanField(_("active"), default=True)
    history = HistoricalRecords()

    def __str__(self):
        """Return string representation of genre"""
        return self.name
    