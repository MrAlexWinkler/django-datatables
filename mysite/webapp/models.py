from django.db import models
from django.db.models.functions import datetime
from django.urls import reverse
from django.contrib.auth.models import User


class Symbol(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Symbol"
        verbose_name_plural = "Symbols"
        ordering = ['name']

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        return super(Symbol, self).save(*args, **kwargs)


class Trade(models.Model):
    class Meta:
        verbose_name = "Trade"
        verbose_name_plural = "Trades"
        ordering = ['-pk']

    # Choices
    OPEN = 'op'
    CLOSED = 'cl'
    PLANNED = 'pl'

    STATUS_CHOICES = [
        (OPEN, 'Open'),
        (CLOSED, 'Closed'),
        (PLANNED, 'Planned')
    ]

    LONG = 'Long'
    SHORT = 'Short'

    TYPE_CHOICES = [
        (LONG, 'Long'),
        (SHORT, 'Short'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='cl')
    type = models.CharField(max_length=5, choices=TYPE_CHOICES, default=LONG)
    symbol = models.ForeignKey(Symbol, on_delete=models.SET_NULL, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('trade-detail', kwargs={'pk': self.pk})


class Entry(models.Model):
    ENTRY = 'entry'
    EXIT = 'exit'
    ENTRY_TYPE_CHOICES = [
        (ENTRY, 'Entry'),
        (EXIT, 'Exit'),
    ]

    class Meta:
        verbose_name = "Entry"
        verbose_name_plural = "Entries"

    trade = models.ForeignKey(Trade, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True, default=datetime.datetime.now)
    amount = models.FloatField(null=True)
    price = models.FloatField(null=True)
    fee = models.FloatField(null=True, blank=True)
    entry_type = models.CharField(max_length=5, choices=ENTRY_TYPE_CHOICES, default=ENTRY)
    reg_fee = models.FloatField(null=True, blank=True)
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    symbol = models.ForeignKey(Symbol, on_delete=models.SET_NULL, blank=True, null=True)
    created_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE)
