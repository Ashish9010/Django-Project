# Generated by Django 4.1 on 2022-11-18 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student_info', '0003_alter_admission_date_admission_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='branch',
            field=models.CharField(choices=[('MECH', 'MECH'), ('ELECTRICAL', 'ELECTRICAL'), ('CHEM', 'Chemical'), ('IT', 'IT'), ('CSE', 'CSE')], max_length=20),
        ),
    ]
