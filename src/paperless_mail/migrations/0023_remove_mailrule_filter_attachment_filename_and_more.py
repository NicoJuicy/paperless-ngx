# Generated by Django 4.2.7 on 2023-11-28 17:47

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("paperless_mail", "0022_mailrule_assign_owner_from_rule_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="mailrule",
            old_name="filter_attachment_filename",
            new_name="filter_attachment_filename_include",
        ),
        migrations.AddField(
            model_name="mailrule",
            name="filter_attachment_filename_exclude",
            field=models.CharField(
                blank=True,
                help_text="Do not consume documents which entirely match this filename if specified. Wildcards such as *.pdf or *invoice* are allowed. Case insensitive.",
                max_length=256,
                null=True,
                verbose_name="filter attachment filename exclusive",
            ),
        ),
    ]
