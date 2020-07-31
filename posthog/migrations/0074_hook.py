# Generated by Django 3.0.6 on 2020-07-31 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("posthog", "0073_personalapikey"),
    ]

    operations = [
        migrations.CreateModel(
            name="Hook",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("event", models.CharField(db_index=True, max_length=64, verbose_name="Event")),
                ("target", models.URLField(max_length=255, verbose_name="Target URL")),
                ("resource_id", models.IntegerField(blank=True, null=True)),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="hooks", to="posthog.Team"
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
    ]
