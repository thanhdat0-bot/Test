from django.contrib import admin
from django.utils.safestring import mark_safe

from courses.models import Course,Category,Lesson

class MyLessonAdmin(admin.ModelAdmin):
    list_display = ['id','subject','created_date']
    search_fields = ['subject']
    list_filter = ['id','created_date']
    list_editable = ['subject']
    readonly_fields = ['image_view']

    def image_view(self,lesson):
        if lesson:
            return mark_safe(f"<img src = '/static/{lesson.image.name}'width = '200' />")

    class Meta:
        css= {
            'all' : ('/static/css/style.css',)
        }

admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Lesson)
# Register your models here.
