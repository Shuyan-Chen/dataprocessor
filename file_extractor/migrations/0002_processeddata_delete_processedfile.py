# Generated by Django 5.0.6 on 2024-06-14 09:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_extractor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessedData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('value', models.FloatField()),
                ('sheet_name', models.CharField(blank=True, max_length=100, null=True)),
                ('row_number', models.PositiveIntegerField(blank=True, null=True)),
                ('column_number', models.PositiveIntegerField(blank=True, null=True)),
                ('uploaded_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='processed_data', to='file_extractor.uploadedfile')),
            ],
        ),
        migrations.DeleteModel(
            name='ProcessedFile',
        ),
    ]
