# Generated by Django 4.2.6 on 2023-11-03 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datademoapp', '0003_signupinfo_dateofbirth_signupinfo_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signupinfo',
            old_name='username',
            new_name='email',
        ),
        migrations.RemoveField(
            model_name='signupinfo',
            name='password',
        ),
    ]
