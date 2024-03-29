from django.contrib import admin
from west.models import Character, Contact, Tag

class TagInline(admin.TabularInline):
    model = Tag

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','age', 'email') # list
    search_fields = ('name',)
    inlines = [TagInline]  # Inline
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes': ('collapse',), # CSS
            'fields': ('age',),
        }]
    )
    
# Register your models here.
admin.site.register(Character)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Tag)