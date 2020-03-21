from django.contrib import admin

# Register your models here.
from .models import Question, Choice

admin.site.site_header="Akash Admin"
admin.site.site_title="Akash admin area"
admin.site.index_title="Welcome to Akash admin area"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

class QuetionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
    ('Date Information', {'fields': ['pub_date'], 'classes':['collapse']}),]
    inlines = [ChoiceInline]


#admin.site.register(Question)
#admin.site.register(Choice)
admin.site.register(Question, QuetionAdmin)