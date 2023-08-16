# Generated by Django 4.2.3 on 2023-08-16 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일시')),
                ('bm_id', models.AutoField(primary_key=True, serialize=False, verbose_name='북마크id')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일시')),
                ('igd_id', models.AutoField(primary_key=True, serialize=False, verbose_name='성분id')),
                ('igd_name', models.CharField(max_length=20, verbose_name='성분명')),
                ('igd_ewg_harzard', models.IntegerField(choices=[(1, 'none'), (2, 'low harzard'), (3, 'moderate harzard'), (4, 'high harzard')], null=True, verbose_name='EWG등급-위험도등급')),
                ('igd_ewg_harzard_no', models.CharField(max_length=10, null=True, verbose_name='EWG등급-위험도숫자')),
                ('igd_ewg_data', models.IntegerField(choices=[(1, 'none'), (2, 'limited'), (3, 'fair'), (4, 'good'), (5, 'robust')], null=True, verbose_name='EWG등급-데이터등급')),
                ('igd_caution', models.BooleanField(default=None, verbose_name='주의성분 포함여부')),
                ('igd_info', models.CharField(default=None, max_length=70, verbose_name='성분 기타 정보')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IngredientProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일시')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingredients.ingredient')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
