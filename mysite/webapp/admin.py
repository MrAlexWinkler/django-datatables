from django.contrib import admin

from .models import *
from django.utils.html import format_html


class EntryTabularInline(admin.TabularInline):
    model = Entry
    extra = 0


class TradeAdmin(admin.ModelAdmin):
    list_display = (
        'get_user', 'user_id', 'pk', 'get_symbol', 'type')
    # inlines = [EntryTabularInline]

    class Meta:
        model = Trade

    def get_symbol(self, instance):
        return format_html("<a target='_blank' href='{0}admin/webapp/symbol/{1}/change'>{2}</a>",
                           admin.site.site_url, instance.symbol_id, instance.symbol)

    get_symbol.short_description = 'Symbol'

    def get_user(self, instance):
        return format_html("<a target='_blank' href='{0}admin/auth/user/{1}/change'>{2}</a>",
                           admin.site.site_url, instance.user_id, instance.user)

    get_user.short_description = 'User'


class SymbolAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


class EntryAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'trade', 'date', 'symbol', 'amount', 'price', 'fee', 'entry_type', 'reg_fee', 'transaction_id',
        'created_by')


# Register your models here.

admin.site.register(Trade, TradeAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Symbol, SymbolAdmin)
