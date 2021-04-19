from django.db import models
from simple_history.models import HistoricalRecords
from django.utils.translation import ugettext_lazy as _
import uuid

class Department(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Name"), max_length=70)    
    description = models.TextField(_("Description"), blank=True, null=True)
    users = models.ForeignKey("users.CustomUser", verbose_name=_("user"), null=True, on_delete=models.SET_NULL)    
    isActive = models.BooleanField(_("active"), default=True)
    history = HistoricalRecords()