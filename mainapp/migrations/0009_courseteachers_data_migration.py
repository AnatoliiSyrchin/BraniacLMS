from django.db import migrations


def forwards_func(apps, schema_editor):
    # Get model
    CourseTeachers = apps.get_model("mainapp", "CourseTeachers")
    Courses = apps.get_model("mainapp", "Courses")
    # Create model's objects
    CourseTeachers.objects.create(
        name_first="Альфред",
        name_second="Нуцубидзе",
        day_birth="1990-07-10",
    ).course.add(1, 3)

    CourseTeachers.objects.create(
        name_first="Роман",
        name_second="Доржинов",
        day_birth="1988-02-04",
    ).course.add(2, 4)

    CourseTeachers.objects.create(
        name_first="Ярослав",
        name_second="Конягин",
        day_birth="1981-12-08",
    ).course.add(3, 5)

    CourseTeachers.objects.create(
        name_first="Автандил",
        name_second="Наварский",
        day_birth="1983-05-16",
    ).course.add(4, 6)

    CourseTeachers.objects.create(
        name_first="Роза",
        name_second="Уланова",
        day_birth="1986-05-09",
    ).course.add(5, 7)

    CourseTeachers.objects.create(
        name_first="Бронислава",
        name_second="Алиева",
        day_birth="1971-01-07",
    ).course.add(6, 8)


def reverse_func(apps, schema_editor):
    # Get model
    CourseTeachers = apps.get_model("mainapp", "Lesson")
    # Delete objects
    CourseTeachers.objects.all().delete()


class Migration(migrations.Migration):

    atomic = False

    dependencies = [
        ("mainapp", "0008_lessons_data_migration"),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
