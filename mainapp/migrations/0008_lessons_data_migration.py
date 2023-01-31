from django.db import migrations


def forwards_func(apps, schema_editor):
    # Get model
    Lessons = apps.get_model("mainapp", "Lesson")
    Courses = apps.get_model("mainapp", "Courses")
    # Create model's objects
    Lessons.objects.create(
        id=11,
        course=Courses.objects.get(id=1),
        num=1,
        title="Lesson 1",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=12,
        course=Courses.objects.get(id=1),
        num=2,
        title="Lesson 2",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=13,
        course=Courses.objects.get(id=1),
        num=3,
        title="Lesson 3",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=14,
        course=Courses.objects.get(id=1),
        num=4,
        title="Lesson 4",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=15,
        course=Courses.objects.get(id=1),
        num=5,
        title="Lesson 5",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=16,
        course=Courses.objects.get(id=1),
        num=6,
        title="Lesson 6",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=17,
        course=Courses.objects.get(id=1),
        num=7,
        title="Lesson 7",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=18,
        course=Courses.objects.get(id=1),
        num=8,
        title="Lesson 8",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=21,
        course=Courses.objects.get(id=2),
        num=1,
        title="Lesson 1",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=22,
        course=Courses.objects.get(id=2),
        num=2,
        title="Lesson 2",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=23,
        course=Courses.objects.get(id=2),
        num=3,
        title="Lesson 3",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=24,
        course=Courses.objects.get(id=2),
        num=4,
        title="Lesson 4",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=25,
        course=Courses.objects.get(id=2),
        num=5,
        title="Lesson 5",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=26,
        course=Courses.objects.get(id=2),
        num=6,
        title="Lesson 6",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=27,
        course=Courses.objects.get(id=2),
        num=7,
        title="Lesson 7",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=28,
        course=Courses.objects.get(id=2),
        num=8,
        title="Lesson 8",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=31,
        course=Courses.objects.get(id=3),
        num=1,
        title="Lesson 1",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=32,
        course=Courses.objects.get(id=3),
        num=2,
        title="Lesson 2",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=33,
        course=Courses.objects.get(id=3),
        num=3,
        title="Lesson 3",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=34,
        course=Courses.objects.get(id=3),
        num=4,
        title="Lesson 4",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=35,
        course=Courses.objects.get(id=3),
        num=5,
        title="Lesson 5",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=36,
        course=Courses.objects.get(id=3),
        num=6,
        title="Lesson 6",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=37,
        course=Courses.objects.get(id=3),
        num=7,
        title="Lesson 7",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=38,
        course=Courses.objects.get(id=3),
        num=8,
        title="Lesson 8",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=41,
        course=Courses.objects.get(id=4),
        num=1,
        title="Lesson 1",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=42,
        course=Courses.objects.get(id=4),
        num=2,
        title="Lesson 2",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=43,
        course=Courses.objects.get(id=4),
        num=3,
        title="Lesson 3",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=44,
        course=Courses.objects.get(id=4),
        num=4,
        title="Lesson 4",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=45,
        course=Courses.objects.get(id=4),
        num=5,
        title="Lesson 5",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=46,
        course=Courses.objects.get(id=4),
        num=6,
        title="Lesson 6",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=47,
        course=Courses.objects.get(id=4),
        num=7,
        title="Lesson 7",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=48,
        course=Courses.objects.get(id=4),
        num=8,
        title="Lesson 8",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=51,
        course=Courses.objects.get(id=5),
        num=1,
        title="Lesson 1",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=52,
        course=Courses.objects.get(id=5),
        num=2,
        title="Lesson 2",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=53,
        course=Courses.objects.get(id=5),
        num=3,
        title="Lesson 3",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=54,
        course=Courses.objects.get(id=5),
        num=4,
        title="Lesson 4",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=55,
        course=Courses.objects.get(id=5),
        num=5,
        title="Lesson 5",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=56,
        course=Courses.objects.get(id=5),
        num=6,
        title="Lesson 6",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=57,
        course=Courses.objects.get(id=5),
        num=7,
        title="Lesson 7",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=58,
        course=Courses.objects.get(id=5),
        num=8,
        title="Lesson 8",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=61,
        course=Courses.objects.get(id=6),
        num=1,
        title="Lesson 1",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=62,
        course=Courses.objects.get(id=6),
        num=2,
        title="Lesson 2",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=63,
        course=Courses.objects.get(id=6),
        num=3,
        title="Lesson 3",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=64,
        course=Courses.objects.get(id=6),
        num=4,
        title="Lesson 4",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=65,
        course=Courses.objects.get(id=6),
        num=5,
        title="Lesson 5",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=66,
        course=Courses.objects.get(id=6),
        num=6,
        title="Lesson 6",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=67,
        course=Courses.objects.get(id=6),
        num=7,
        title="Lesson 7",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=68,
        course=Courses.objects.get(id=6),
        num=8,
        title="Lesson 8",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=71,
        course=Courses.objects.get(id=7),
        num=1,
        title="Lesson 1",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=72,
        course=Courses.objects.get(id=7),
        num=2,
        title="Lesson 2",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=73,
        course=Courses.objects.get(id=7),
        num=3,
        title="Lesson 3",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=74,
        course=Courses.objects.get(id=7),
        num=4,
        title="Lesson 4",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=75,
        course=Courses.objects.get(id=7),
        num=5,
        title="Lesson 5",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=76,
        course=Courses.objects.get(id=7),
        num=6,
        title="Lesson 6",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=77,
        course=Courses.objects.get(id=7),
        num=7,
        title="Lesson 7",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=78,
        course=Courses.objects.get(id=7),
        num=8,
        title="Lesson 8",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=81,
        course=Courses.objects.get(id=8),
        num=1,
        title="Lesson 1",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=82,
        course=Courses.objects.get(id=8),
        num=2,
        title="Lesson 2",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=83,
        course=Courses.objects.get(id=8),
        num=3,
        title="Lesson 3",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=84,
        course=Courses.objects.get(id=8),
        num=4,
        title="Lesson 4",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=85,
        course=Courses.objects.get(id=8),
        num=5,
        title="Lesson 5",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=86,
        course=Courses.objects.get(id=8),
        num=6,
        title="Lesson 6",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=87,
        course=Courses.objects.get(id=8),
        num=7,
        title="Lesson 7",
        description="Описание урока",
    )

    Lessons.objects.create(
        id=88,
        course=Courses.objects.get(id=8),
        num=8,
        title="Lesson 8",
        description="Описание урока",
    )


def reverse_func(apps, schema_editor):
    # Get model
    Lessons = apps.get_model("mainapp", "Lesson")
    # Delete objects
    Lessons.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0007_news_data_migration"),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
