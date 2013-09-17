from django.contrib import admin
from pastebin.models import Paste
from datetime import date

class ExpiredListFilter(admin.SimpleListFilter):

    title = u"Expiration"
    parameter_name = "expiration_date"

    def lookups(self, request, model_admin):
        return (
            ('yes', u'expired'),
            ('no', u'actual'),
        )

    def queryset(self, request, queryset):
        if self.value == 'yes':
            return queryset.filter(expiration_date__lt=date.today())
        if self.value == 'no':
            return queryset.filter(expiration_date__gte=date.today())


class AuthExpiredListFilter(ExpiredListFilter):
    
    def lookups(self, request, model_admin):
        if request.user.is_superuser:
            return super(AuthExpiredListFilter, self).lookups(request, model_admin)

    def queryset(self, request, queryset):
        if request.user.is_superuser:
            return super(AuthExpiredListFilter, self).queryset(request, queryset)


class PasteAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    fields = ('author', 'title', 'content', 'syntax', 'expiration_date')
    list_display = ('title', 'author', 'syntax', 'is_expired')
    list_display_links = ('title',)
    list_filter = (AuthExpiredListFilter,)


admin.site.register(Paste, PasteAdmin)
