# Generated by Django 4.1.7 on 2023-04-10 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0002_note_delete_book_delete_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
