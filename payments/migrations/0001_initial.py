# Generated by Django 3.2.16 on 2022-12-13 05:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('deleted_at', models.DateField()),
                ('name', models.CharField(max_length=50, verbose_name='discount name')),
                ('description', models.TextField(verbose_name='discount description')),
                ('discount_percent', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='discount percent')),
                ('active', models.BooleanField(verbose_name='discount active')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
