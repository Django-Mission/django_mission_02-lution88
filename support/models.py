from turtle import title
from django.db import models
from django.contrib.auth import get_user_model
from posts.models import User
# Create your models here.

class Faq(models.Model):
    question = models.CharField(max_length=250, verbose_name='질문')
    CATEGORY_CHOICES = [
        ('일반', '일반'),
        ('계정', '계정'),
        ('기타', '기타'),
    ]
    category = models.CharField(max_length=2, verbose_name='카테고리' ,choices=CATEGORY_CHOICES)
    answer = models.TextField(verbose_name='답변', null=True, blank=True)
    author = models.ForeignKey(to=User, verbose_name='생성자', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일')
    updated_person = models.CharField(max_length=30, verbose_name='최종수정자')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='최종수정일시')

class Inquiry(models.Model):
    # TITLE_CHOICES=[
    #     ('일반', '일반'),
    #     ('계정', '계정'),
    #     ('기타', '기타'),
    # ]
    title = models.CharField(max_length=50, verbose_name='제목') 
    email = models.EmailField(verbose_name='이메일', null=True, blank=True)
    message = models.IntegerField(verbose_name='문자메시지', null=True, blank=True)
    content = models.TextField(verbose_name='내용')
    image = models.ImageField(verbose_name='이미지', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='생성일', auto_now_add=True)

class Answer(models.Model):
    answer = models.TextField(verbose_name='답변내용')
    inquiry = models.ForeignKey(Inquiry, on_delete=models.CASCADE, verbose_name='참조문의글')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='생성자')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일시')
    updated_person = models.CharField(max_length=30, verbose_name='최종수정자')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='최종수정일')