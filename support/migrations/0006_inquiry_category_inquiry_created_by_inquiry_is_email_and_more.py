# Generated by Django 4.0.3 on 2022-04-29 03:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('support', '0005_inquiry_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquiry',
            name='category',
            field=models.CharField(choices=[('1', '일반'), ('2', '계정'), ('3', '기타')], default='', max_length=2, verbose_name='카테고리'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inquiry',
            name='created_by',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='inquiry_created_by', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inquiry',
            name='is_email',
            field=models.BooleanField(default=False, verbose_name='이메일 수신 여부'),
        ),
        migrations.AddField(
            model_name='inquiry',
            name='is_message',
            field=models.BooleanField(default=False, verbose_name='문자메세지 수신 여부'),
        ),
        migrations.AddField(
            model_name='inquiry',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='수정일'),
        ),
        migrations.AddField(
            model_name='inquiry',
            name='updated_by',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='inquiry_updated_by', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_created_by', to=settings.AUTH_USER_MODEL, verbose_name='생성자'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='updated_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='최종수정자'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='faq_created_by', to=settings.AUTH_USER_MODEL, verbose_name='생성자'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='faq',
            name='updated_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faq_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='최종수정자'),
        ),
    ]