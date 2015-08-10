from django.contrib import admin
from core.models import ToDo

class ToDoAdmin(admin.ModelAdmin):
    list_display = ('propietario','todo','hecho')
    exclude = ('propietario',)

    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """
        obj.propietario = request.user
        obj.save()

admin.site.register(ToDo,ToDoAdmin)
