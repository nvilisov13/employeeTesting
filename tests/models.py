from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class EmployeesTest(models.Model):
    NameTest = models.CharField(max_length=50, verbose_name='Название теста')
    DescriptionTest = models.TextField(blank=True, verbose_name='Описание теста')

    class Meta:
        verbose_name = 'тест сотрудников'
        verbose_name_plural = 'Тесты сотрудников'


class Questions(models.Model):
    TextQuestion = models.TextField(verbose_name='Текст вопроса')
    ImageQuestion = models.ImageField(upload_to="images_questions", default=None,
                                      blank=True, null=True, verbose_name='Изображение вопроса')
    TestNum = models.ForeignKey(EmployeesTest, on_delete=models.CASCADE, verbose_name='Номер теста')

    class Meta:
        verbose_name = 'вопрос теста'
        verbose_name_plural = 'Вопросы теста'


@receiver(pre_save, sender=Questions)
def set_image_filename(sender, instance, **kwargs):
    if instance.pk and instance.ImageQuestion:
        instance.ImageQuestion.name = f"{instance.pk}_{instance.ImageQuestion.name}"


class AnswerQuestions(models.Model):
    TextAnswer = models.TextField(verbose_name='Текст ответа')
    MarkAnswer = models.SmallIntegerField(default=0, verbose_name='Количество баллов за ответ')
    Question = models.ForeignKey(Questions, on_delete=models.CASCADE, verbose_name='Ответ на вопрос')

    class Meta:
        verbose_name = 'ответы на вопрос'
        verbose_name_plural = 'Ответы на вопросы'


class Employees(models.Model):
    FirstName = models.CharField(max_length=30, verbose_name='Имя')
    LastName = models.CharField(max_length=30, verbose_name='Фамилия')
    Phone = models.CharField(max_length=12, null=True, verbose_name='Телефон')
    TelegramID = models.CharField(max_length=12, null=True, verbose_name='ID пол-я телеграмма')

    class Meta:
        verbose_name = 'сотрудника'
        verbose_name_plural = 'сотрудники'


class NominatedTests(models.Model):
    MarksTest = models.SmallIntegerField(blank=True, null=True, verbose_name='Оценка за тест')
    SinceDateTime = models.DateTimeField(blank=True, null=True, verbose_name='Дата/время начало прохождения теста')
    DuringDateTime = models.DateTimeField(blank=True, null=True, verbose_name='Дата/время завершения прохождения теста')
    Employee = models.ForeignKey(Employees, on_delete=models.CASCADE, verbose_name='Сотрудник')
    Test = models.ForeignKey(EmployeesTest, null=True, on_delete=models.SET_NULL, verbose_name='Тест')

    class Meta:
        verbose_name = 'назначенный тест'
        verbose_name_plural = 'Назначенные тесты'
