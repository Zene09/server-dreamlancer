# Generated by Django 4.1 on 2022-08-22 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_contract_jobtype_alter_contract_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='jobtype',
            field=models.CharField(choices=[('UI', 'UI'), ('UX', 'UX'), ('FE', 'Front End'), ('BE', 'Back End'), ('FS', 'Full Stack'), ('RE', 'Refactor')], default=None, max_length=2),
        ),
    ]
