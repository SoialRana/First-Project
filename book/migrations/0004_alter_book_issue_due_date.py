# Generated by Django 4.2.3 on 2023-09-07 10:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_book_issue_students_remove_review_book_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_issue',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 15, 16, 22, 12, 757213)),
        ),
    ]
