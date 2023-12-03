from django.contrib import admin
from  .models import *
# Register your models here.
class contactusAdmin(admin.ModelAdmin):
    list_display = ('Name','Mobile','Email','Message')

admin.site.register(contactus,contactusAdmin)

###################################################
class categoryAdmin(admin.ModelAdmin):
    list_display =('id','Name','CPic')
admin.site.register(category,categoryAdmin)
###################################################
class maincateAdmin(admin.ModelAdmin):
    list_display=('id','Name','picture','cdate')
admin.site.register(maincate,maincateAdmin)
############################################################

class uregisterAdmin(admin.ModelAdmin):
    list_display = ('name','mobile','email','userpic','passwd','message')
admin.site.register(uregister,uregisterAdmin)



##################################################
class myproductAdmin(admin.ModelAdmin):
    list_display=('id','pcategory','pprice','psize','pcolor','pdate','pdes','dprice','ppic','pdel')

admin.site.register(myproduct,myproductAdmin)

class mcartAdmin(admin.ModelAdmin):
    list_display=('id','userid','pid','cdate','status')
admin.site.register(mcart,mcartAdmin)

class morderAdmin(admin.ModelAdmin):
    list_display=('id','userid','pid','status','odate','remarks')
admin.site.register(morder,morderAdmin)

