import random
import string

from django.db import models, transaction

__all__ = ("URLMapping",)

class URLMapping(models.Model):
    class Meta:
        ordering = ('-pk',)

    url = models.URLField()
    short = models.CharField(
        max_length=8,
        unique=True,
        db_index=True,
        blank=True,
        editable=False
    )

    def __str__(self):
        return f"{self.short} -> {self.url}"

    @staticmethod
    def get_short():
        """Zwraca losowy 8-znakowy ciąg znaków."""
        return "".join(random.choices(string.ascii_letters, k=8))

    @classmethod
    def short_exists(cls, short):
        """Sprawdza, czy istnieje już rekord z podanym krótkim URL."""
        return cls.objects.filter(short=short).exists()

    @transaction.atomic()
    def save(self, *args, **kwargs):
        """Nadaje pierwszy wolny unikalny short."""
        while not self.short and not self.short_exists(self.short):
            self.short = URLMapping.get_short()

        # Walidacja URL
        self.full_clean()
        super().save(*args, **kwargs)
