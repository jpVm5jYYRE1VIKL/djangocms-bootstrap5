from django.db import models
from django.utils.translation import gettext_lazy as _

from djangocms_icon.fields import Icon
from djangocms_link.models import AbstractLink

from djangocms_bootstrap5.constants import COLOR_STYLE_CHOICES

from .constants import LINK_CHOICES, LINK_SIZE_CHOICES


# 'link' type is added manually as it is only required for this plugin
COLOR_STYLE_CHOICES = (
    ('link', _('Link')),
) + COLOR_STYLE_CHOICES


class Bootstrap5Link(AbstractLink):
    """
    Components > "Button" Plugin
    https://getbootstrap.com/docs/5.0/components/buttons/
    """
    link_type = models.CharField(
        verbose_name=_('Type'),
        choices=LINK_CHOICES,
        default=LINK_CHOICES[0][0],
        max_length=255,
        help_text=_('Adds either the .btn-* or .text-* classes.'),
    )
    link_context = models.CharField(
        verbose_name=_('Context'),
        choices=COLOR_STYLE_CHOICES,
        blank=True,
        max_length=255,
    )
    link_size = models.CharField(
        verbose_name=_('Size'),
        choices=LINK_SIZE_CHOICES,
        blank=True,
        max_length=255,
    )
    link_outline = models.BooleanField(
        verbose_name=_('Outline'),
        default=False,
        help_text=_('Applies the .btn-outline class to the elements.'),
    )
    icon_left = Icon(
        verbose_name=_('Icon left'),
    )
    icon_right = Icon(
        verbose_name=_('Icon right'),
    )

    def __str__(self):
        return str(self.pk)
