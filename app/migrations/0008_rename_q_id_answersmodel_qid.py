# Generated by Django 5.0.3 on 2024-03-15 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_questionsmodel_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answersmodel',
            old_name='q_id',
            new_name='qid',
        ),
    ]
