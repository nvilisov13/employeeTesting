# Generated by Django 4.1.10 on 2024-04-23 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=30, verbose_name='Имя')),
                ('LastName', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('Phone', models.CharField(max_length=12, null=True, verbose_name='Телефон')),
                ('TelegramID', models.CharField(max_length=12, null=True, verbose_name='ID пол-я телеграмма')),
            ],
            options={
                'verbose_name': 'сотрудника',
                'verbose_name_plural': 'сотрудники',
            },
        ),
        migrations.CreateModel(
            name='EmployeesTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameTest', models.CharField(max_length=50, verbose_name='Название теста')),
                ('DescriptionTest', models.TextField(blank=True, verbose_name='Описание теста')),
            ],
            options={
                'verbose_name': 'тест сотрудников',
                'verbose_name_plural': 'Тесты сотрудников',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TextQuestion', models.TextField(verbose_name='Текст вопроса')),
                ('ImageQuestion', models.ImageField(blank=True, default=None, null=True, upload_to='images_questions', verbose_name='Изображение вопроса')),
                ('TestNum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.employeestest', verbose_name='Номер теста')),
            ],
            options={
                'verbose_name': 'вопрос теста',
                'verbose_name_plural': 'Вопросы теста',
            },
        ),
        migrations.CreateModel(
            name='NominatedTests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MarksTest', models.SmallIntegerField(blank=True, null=True, verbose_name='Оценка за тест')),
                ('SinceDateTime', models.DateTimeField(blank=True, null=True, verbose_name='Дата/время начало прохождения теста')),
                ('DuringDateTime', models.DateTimeField(blank=True, null=True, verbose_name='Дата/время завершения прохождения теста')),
                ('Employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.employees', verbose_name='Сотрудник')),
                ('Test', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tests.employeestest', verbose_name='Тест')),
            ],
            options={
                'verbose_name': 'назначенный тест',
                'verbose_name_plural': 'Назначенные тесты',
            },
        ),
        migrations.CreateModel(
            name='AnswerQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TextAnswer', models.TextField(verbose_name='Текст ответа')),
                ('MarkAnswer', models.SmallIntegerField(default=0, verbose_name='Количество баллов за ответ')),
                ('Question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.questions', verbose_name='Ответ на вопрос')),
            ],
            options={
                'verbose_name': 'ответы на вопрос',
                'verbose_name_plural': 'Ответы на вопросы',
            },
        ),
    ]
