# Generated by Django 4.2.3 on 2023-07-07 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0097_alter_channel_kind"),
    ]

    operations = [
        migrations.AddField(
            model_name="channel",
            name="last_notify_duration",
            field=models.DurationField(blank=True, null=True),
        ),
    ]
