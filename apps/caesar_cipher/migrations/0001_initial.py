# Generated by Django 4.2 on 2023-04-07 17:42

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MessageModel",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("text", models.TextField(max_length=250)),
                ("text_crypto", models.TextField(max_length=250)),
                ("key_step", models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
