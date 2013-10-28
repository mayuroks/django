from django.contrib import admin
from models import Post, Colin
from import_export.admin import ImportExportModelAdmin

class PostAdmin(ImportExportModelAdmin):pass
admin.site.register(Post, PostAdmin)

class ColinAdmin(ImportExportModelAdmin):pass
admin.site.register(Colin, ColinAdmin)