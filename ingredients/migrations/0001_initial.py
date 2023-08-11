# Generated by Django 4.2.3 on 2023-08-10 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일시')),
                ('igd_id', models.AutoField(primary_key=True, serialize=False, verbose_name='성분id')),
                ('igd_name', models.CharField(max_length=20, verbose_name='성분명')),
                ('igd_main_ftn', models.TextField(verbose_name='성분메인기능')),
                ('igd_plants', models.BooleanField(null=True, verbose_name='식물성')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일시')),
                ('bm_id', models.AutoField(primary_key=True, serialize=False, verbose_name='북마크id')),
                ('igd', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ingredients.ingredient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bm_igd_id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
