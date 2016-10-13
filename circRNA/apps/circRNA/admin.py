from django.contrib import admin
from circRNA.apps.circRNA.models import circRNA

class circRNAAdmin(admin.ModelAdmin):
    """ """
    search_fields = ['circRNA_ID',]

        
admin.site.register(circRNA, circRNAAdmin)