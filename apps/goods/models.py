from django.db import models
from datetime import datetime


class MyLookupType(models.Model):
    """
    lookup type
    """
    lookup_type = models.CharField(max_length=120, null=True, verbose_name="lookup_type")
    enable_flag = models.BooleanField(default=True, verbose_name="enable_flag")
    language = models.CharField(max_length=45, verbose_name="language")
    creation_date = models.DateTimeField(default=datetime.now, verbose_name="creation_date")

    class Meta:
        verbose_name = 'MyLookupType'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.lookup_type


class MyLookupValue(models.Model):
    """
    lookup value
    """
    lookup_type_id = models.ForeignKey(MyLookupType, null=True, on_delete=models.CASCADE, verbose_name="lookup_type_id")
    lookup_code = models.CharField(max_length=240, null=True, verbose_name="lookup_code")
    language = models.CharField(max_length=45, verbose_name="language")
    display_sequence = models.IntegerField(default=1, blank=True, null=True, verbose_name="data increment")

    # def save(self, *args, **kwargs):
    #     if self._state.adding:
    #         last_id = self.objects.all().aggregate(largest=models.Max('display_sequence'))['largest']
    #         if last_id is not None:
    #             self.display_sequence = last_id + 1
    #     super(MyLookupValue, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'MyLookupValue'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.lookup_code
