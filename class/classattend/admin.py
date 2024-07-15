from django.contrib import admin
from .models import Attendance

# Register your models here.

class AttendanceInline(admin.TabularInline):
     model = Attendance
     raw_id_fields = ['attendances']
     
     
     
class AttendanceAdmin(admin.ModelAdmin):
     list_display = ['id','firstName', 'lastName', 'email' 'course']
      
     list_filter = [ 'updated', 'created']
     inlines = [AttendanceInline]



admin.site.register(Attendance)