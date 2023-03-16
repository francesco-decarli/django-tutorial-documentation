from django.contrib import admin
from .models import Question, Choice

# Register your models here.
class ChoiceInLine(admin.TabularInline):    # StackedInLine is another way to do it but, in this case, Tabular mode is more conpact
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')        # inlines = [ChoiceInLine]
    # Adds a Filiter sidebar that lets filtering by pub_date field
    list_filter = ['pub_date']
    # Search box for the question field
    search_fields = ['question_text']
    # Number of elements displayed on each paginated admin change list page
    list_per_page = 10

    # Previously on
    # fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)