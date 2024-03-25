# Generated by Django 3.2.4 on 2021-07-22 13:25

from __future__ import annotations

from typing import Any

from django.apps.registry import Apps
from django.db import migrations


def fill_member_role(apps: Apps, schema_editor: Any) -> None:
    Member = apps.get_model("accounts", "Member")
    Member.objects.filter(rw=False).update(role="r")
    Member.objects.filter(rw=True).update(role="w")


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0040_auto_20210722_1244"),
    ]

    operations = [
        migrations.RunPython(fill_member_role, migrations.RunPython.noop),
    ]