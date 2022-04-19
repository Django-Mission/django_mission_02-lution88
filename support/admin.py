from django.contrib import admin
from .models import Answer, Faq, Inquiry
# Register your models here.

@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'question','category','author', 'created_at', 'updated_at')
    list_filter = ('updated_at',)

@admin.register(Inquiry)
class InquiryModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at')

@admin.register(Answer)
class AnswerModelAdmin(admin.ModelAdmin):
    list_display = ('id','answer','inquiry', 'created_at','updated_at')
