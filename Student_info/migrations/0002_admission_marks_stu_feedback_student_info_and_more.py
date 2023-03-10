# Generated by Django 4.1 on 2022-11-17 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Student_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('Class', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('branch', models.CharField(choices=[('MECH', 'MECH-Type'), ('ELECTRICAL', 'ELECTRICAL-Type'), ('CHEM', 'Chemical-Type'), ('IT', 'IT-Type'), ('CSE', 'CSE-Type')], max_length=50)),
                ('Year', models.IntegerField(default=2022)),
                ('Date_Admission', models.DateTimeField(auto_now_add=True)),
                ('Semester', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Totalmarks', models.IntegerField()),
                ('Semester', models.CharField(max_length=10)),
                ('Year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stu_Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('Subject', models.CharField(choices=[('TOC', 'TOC'), ('PYTHON', 'PYTHON'), ('SOFTWARE ENGINEERING', 'SOFTWARE ENGINEERING'), ('OS', 'OS'), ('DBMS', 'DBMS')], max_length=250)),
                ('Feedback_stu', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Student_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Studentname', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, upload_to='users/%Y/%m/%d/')),
                ('RegNO', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('Taluka', models.CharField(max_length=15)),
                ('District', models.CharField(max_length=15)),
                ('pincode', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='fees',
            name='reg_NO',
        ),
        migrations.DeleteModel(
            name='attendance',
        ),
        migrations.DeleteModel(
            name='Fees',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.AddField(
            model_name='stu_feedback',
            name='regNO',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student_info.student_info'),
        ),
        migrations.AddField(
            model_name='marks',
            name='regNO',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student_info.student_info'),
        ),
        migrations.AddField(
            model_name='admission',
            name='nameStudent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Studentname_Student_set', to='Student_info.student_info'),
        ),
        migrations.AddField(
            model_name='admission',
            name='regNO',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='RegNO_Student_set', to='Student_info.student_info'),
        ),
    ]
