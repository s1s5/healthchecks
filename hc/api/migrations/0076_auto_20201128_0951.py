# Generated by Django 3.1.2 on 2020-11-28 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0075_auto_20200805_1004"),
    ]

    operations = [
        migrations.AddField(
            model_name="ping",
            name="exitstatus",
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="channel",
            name="kind",
            field=models.CharField(
                choices=[
                    ("email", "Email"),
                    ("webhook", "Webhook"),
                    ("hipchat", "HipChat"),
                    ("slack", "Slack"),
                    ("pd", "PagerDuty"),
                    ("pagertree", "PagerTree"),
                    ("pagerteam", "Pager Team"),
                    ("po", "Pushover"),
                    ("pushbullet", "Pushbullet"),
                    ("opsgenie", "OpsGenie"),
                    ("victorops", "VictorOps"),
                    ("discord", "Discord"),
                    ("telegram", "Telegram"),
                    ("sms", "SMS"),
                    ("zendesk", "Zendesk"),
                    ("trello", "Trello"),
                    ("matrix", "Matrix"),
                    ("whatsapp", "WhatsApp"),
                    ("apprise", "Apprise"),
                    ("mattermost", "Mattermost"),
                    ("msteams", "Microsoft Teams"),
                    ("shell", "Shell Command"),
                    ("zulip", "Zulip"),
                    ("spike", "Spike"),
                    ("call", "Phone Call"),
                    ("linenotify", "LINE Notify"),
                ],
                max_length=20,
            ),
        ),
    ]