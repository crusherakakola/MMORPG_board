# Generated by Django 4.2.4 on 2023-09-15 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0008_remove_comment_article_delete_article_delete_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reply',
            old_name='response',
            new_name='response_reply',
        ),
    ]
