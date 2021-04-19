from django.db import models
from simple_history.models import HistoricalRecords

class Tools(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Name"), max_length=70)
    identification = models.CharField(_("Identification"), max_length=50, blank=True, null=True)
    description = models.TextField(_("Description"), blank=True, null=True)
    keeper = models.ForeignKey("users.CustomUser", verbose_name=_("keeper"), on_delete=models.SET_NULL)
    department = models.ForeignKey("bratool.Department", verbose_name=_("department"), on_delete=models.SET_NULL)
    models.ImageField(_("Image"), upload_to='tools/%Y/%m/%d/', blank=True, null=True)
    isActive = models.BooleanField(_("active"), default=True)
    history = HistoricalRecords()

class Genre(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Name"), max_length=70)    
    description = models.TextField(_("Description"), blank=True, null=True)    
    tools = models.ForeignKey("tools.Tools", verbose_name=_("tool"), on_delete=models.SET_NULL)
    departments = models.ForeignKey("bratool.Department", verbose_name=_("department"), on_delete=models.SET_NULL)    
    isActive = models.BooleanField(_("active"), default=True)
    history = HistoricalRecords()