from django.db.models import (
Model,
CharField,
TextChoices,
IntegerChoices,
)
from django.utils.translations import gettext_lazy as _

class Apartment(Model):
	class HouseType(TextChoices):
		HOUSE = "HS", _("House")
		CONDO= "CD", _("Condominium")
		CO_OP= "CO", _("Housing Cooperative")
		APARTMENT= "AP", _("Apartment")
		TOWNHOUSE= "TH", _("Townhouse")
		MANUFACTURED= "MN", _("Manufactured Home")
		MULTI_FAMILY= "MF", _("Multi-Family Home")
		LOT= "LT", _("Lot")
		LAND= "LD", _("Land")
		

