# Generated by Django 4.1.6 on 2023-02-25 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_alter_student_mess_alter_student_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='mess',
            field=models.ImageField(null=True, upload_to='messphotos/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos/'),
        ),
    ]
