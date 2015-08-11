from django.contrib import admin
from core.models import ToDo,TypeCard,Card,Transaction,UserPerfil

class ToDoAdmin(admin.ModelAdmin):
    list_display = ('propietario','todo','hecho')
    exclude = ('propietario',)

    def save_model(self, request, obj, form, change):
        obj.propietario = request.user
        obj.save()

class CardAdmin(admin.ModelAdmin):
    list_display = ('type_card','owner','number_card','available')
    exclude = ('owner',)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        obj.save()

class UserPerfilAdmin(admin.ModelAdmin):
    list_display = ('id','user','is_company','code')
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('card','collect','amount')

    def save_model(self, request, obj, form, change):
        obj.save()


admin.site.register(ToDo,ToDoAdmin)
admin.site.register(Card,CardAdmin)
admin.site.register(UserPerfil,UserPerfilAdmin)
admin.site.register(TypeCard)
admin.site.register(Transaction,TransactionAdmin)



