from django.db import models
from django.urls import reverse


class Country(models.Model):

    name = models.CharField(
        max_length=256, db_index=True, verbose_name="Назва країни")

    class Meta:
        verbose_name = "Країна"
        verbose_name_plural = "Країни"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("country_detail", kwargs={"pk": self.pk})


class Company(models.Model):

    short_name = models.CharField(
        max_length=256, db_index=True, verbose_name="Коротка назва")

    full_name = models.CharField(
        max_length=256, verbose_name="Повна назва", blank=True)

    country = models.ForeignKey(Country)

    class Meta:
        verbose_name = "Підприємство"
        verbose_name_plural = "Підприємства"

    def __str__(self):
        return self.short_name

    def get_absolute_url(self):
        return reverse("company_detail", kwargs={"pk": self.pk})

    @property
    def talks(self):
        return self.talk.all()


class Talk(models.Model):

    date = models.DateTimeField(verbose_name="Дата")

    company = models.ForeignKey(Company, related_name="talk")

    source_info = models.TextField(verbose_name="Інфо про джерело")

    talk_details = models.TextField(verbose_name="Інфо про розмову")

    is_our_talk = models.BooleanField(default=False,
                                      verbose_name="Ми звернулися")

    class Meta:
        verbose_name = "Розмова"
        verbose_name_plural = "Розмови"
        ordering = ['-date']

    def __str__(self):
        return "{} / {}".format(self.date, self.company)

    def get_absolute_url(self):
        return reverse("talk_detail", kwargs={"pk": self.pk})
