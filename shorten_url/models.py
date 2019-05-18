from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from id_encoder import encode_and_enbase


class Redirect(models.Model):
    visits = models.IntegerField(default=0, null=False)
    destination = models.URLField()
    code = models.TextField(
        unique=True,
        max_length=254,
        null=True,
        blank=True,
        editable=False
    )

    # pylint: disable=no-member
    def generate_code(self):
        self.code = encode_and_enbase(self.id)


# pylint: disable=unused-argument
@receiver(post_save, sender=Redirect)
def model_created_or_updated(sender, **kwargs):
    the_instance = kwargs['instance']
    if not the_instance.code:
        the_instance.generate_code()
        the_instance.save()
