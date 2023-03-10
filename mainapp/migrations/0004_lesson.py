import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("mainapp", "0003_news")]

    operations = [
        migrations.CreateModel(
            name="Lesson",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("num", models.PositiveIntegerField(verbose_name="Lesson number")),
                ("title", models.CharField(max_length=256, verbose_name="Name")),
                ("description", models.TextField(blank=True, null=True, verbose_name="Description")),
                ("description_as_markdown", models.BooleanField(default=False, verbose_name="As markdown")),
                ("created", models.DateTimeField(auto_now_add=True, verbose_name="Created")),
                ("updated", models.DateTimeField(auto_now=True, verbose_name="Edited")),
                ("deleted", models.BooleanField(default=False)),
                ("course", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="mainapp.courses")),
            ],
        ),
    ]
