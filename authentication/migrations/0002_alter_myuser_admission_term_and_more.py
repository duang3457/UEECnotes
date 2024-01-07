# Generated by Django 4.2.7 on 2024-01-04 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='admission_term',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='admission_year',
            field=models.IntegerField(choices=[(2023, 'before 2024'), (2024, '2024'), (2025, '2025'), (2026, '2026'), (2027, 'after 2026')], null=True),
        ),
    ]
