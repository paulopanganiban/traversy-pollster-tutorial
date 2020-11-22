from django.contrib import admin

# Register your models here.
from .models import Question, Choice
# lagay mo dito yung gusto mo isama sa admin area

# change site header and title

admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.site_index = "Welcome to the Pollster Admin Area"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
    # yung hanging coma ay tuple sa python. research about this
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)

msg = "Hello word"
