from django.contrib import admin
from .models import Question
from .models import Choice

# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2
    list_display = ('question_text',)

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['text']}),
    ]
    inlines = [ChoiceInline]

# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)