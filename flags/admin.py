from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from .models import FlaggedContent, FlagInstance

class InlineFlagInstance(admin.TabularInline):
    model = FlagInstance
    extra = 0

class FlaggedListFilter(admin.SimpleListFilter):
    title = 'Content Type'
    parameter_name='content_type'
    def lookups(self, request, model_admin):

        return ContentType.objects.filter(id__in=FlaggedContent.objects.values('content_type_id')).values_list('id','name')

    def queryset(self, request, queryset):
        if request.GET:
            return queryset.filter(content_type=request.GET.get(self.parameter_name))
        else:
            return queryset.all()


class FlaggedContentAdmin(admin.ModelAdmin):
    inlines = [InlineFlagInstance]
    list_display = ['content_object', 'content_type', 'instances']
    list_filter = (FlaggedListFilter,)

    def instances(self, obj):
        return obj.flaginstance_set.count()

admin.site.register(FlaggedContent, FlaggedContentAdmin)
