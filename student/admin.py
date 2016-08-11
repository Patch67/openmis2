from django.contrib import admin
from import_export import resources

from .models import Student

from import_export.admin import ImportExportModelAdmin


# Hopefully add import / export facilities to the admin page
class StudentAdmin(ImportExportModelAdmin):
    pass


# Setup import_export
# See https://django-import-export.readthedocs.io/en/latest/getting_started.html
class StudentResource(resources.ModelResource):

    class Meta:
        model = Student
        # These are the fields I want to import
        fields = ('id', 'first_name', 'last_name', 'date_of_birth', 'ULN')
        # Added this to accept UK formatted date (dd/mm/yyyy)
        widgets = {
            'date_of_birth': {'format': '%dd/%mm/%yyyy'},
        }
        # This is the order for export
        export_order = ('id', 'first_name', 'last_name', 'date_of_birth', 'ULN')
        # Let me know what's happening
        skip_unchanged = True
        report_skipped = True

# Mega Important: Will not work until you register StudentAdmin with admin site
admin.site.register(Student, StudentAdmin)
