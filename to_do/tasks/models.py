from django.contrib.auth.models import \
    User  # Импортируем стандартную модель User Django для связи с пользователями
from django.db import \
    models  # Импортируем модуль models для работы с моделями Django


# Модель Priority (Приоритет)
class Priority(models.Model):
    name = models.CharField(
        max_length=255, verbose_name="Название"
    )  # Поле для названия приоритета, CharField - текстовое поле
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )  # Поле для даты создания, DateTimeField - дата и время, auto_now_add=True - автоматически устанавливает текущее время при создании
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата обновления"
    )  # Поле для даты обновления, auto_now=True - автоматически устанавливает текущее время при каждом изменении
    deleted_at = models.DateTimeField(
        null=True, blank=True, verbose_name="Дата удаления"
    )  # Поле для даты удаления, может быть пустым (null=True) и не обязательным для заполнения (blank=True)
    deleted = models.BooleanField(
        default=False, verbose_name="Удален"
    )  # Поле для отметки удаления, BooleanField - логическое поле, default=False - по умолчанию не удалено

    def __str__(
        self,
    ):  # Метод для отображения названия приоритета в админ-панели и других местах
        return self.name

    class Meta:  # Метаданные модели
        verbose_name = "Приоритет"  # Название модели в единственном числе
        verbose_name_plural = "Приоритеты"  # Название модели во множественном числе


# Модель Category (Категория)
class Category(models.Model):
    name = models.CharField(
        max_length=255, verbose_name="Название"
    )  # Поле для названия категории
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание"
    )  # Поле для описания категории, может быть пустым
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )  # Поле для даты создания
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата обновления"
    )  # Поле для даты обновления
    deleted_at = models.DateTimeField(
        null=True, blank=True, verbose_name="Дата удаления"
    )  # Поле для даты удаления
    deleted = models.BooleanField(
        default=False, verbose_name="Удалена"
    )  # Поле для отметки удаления

    def __str__(self):  # Метод для отображения названия категории
        return self.name

    class Meta:  # Метаданные модели
        verbose_name = "Категория"  # Название модели в единственном числе
        verbose_name_plural = "Категории"  # Название модели во множественном числе


# Модель Task (Задача)
class Task(models.Model):
    STATUS_CHOICES = (  # Кортеж с возможными статусами задачи
        ("pending", "В ожидании"),
        ("in_progress", "В процессе"),
        ("completed", "Завершено"),
    )

    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Кем создана"
    )  # Связь с моделью User, ForeignKey - внешний ключ, on_delete=models.CASCADE - при удалении пользователя удаляются и его задачи
    title = models.CharField(
        max_length=255, verbose_name="Название"
    )  # Поле для названия задачи
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание"
    )  # Поле для описания задачи, может быть пустым
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="pending", verbose_name="Статус"
    )  # Поле для статуса задачи, CharField с выбором из STATUS_CHOICES, default='pending' - по умолчанию "В ожидании"
    completed = models.BooleanField(
        default=False, verbose_name="Завершена"
    )  # Поле для отметки выполнения задачи
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )  # Поле для даты создания
    completed_at = models.DateTimeField(
        blank=True, null=True, verbose_name="Дата завершения"
    )  # Поле для даты завершения, может быть пустым
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата обновления"
    )  # Поле для даты обновления
    deleted_at = models.DateTimeField(
        blank=True, null=True, verbose_name="Дата удаления"
    )  # Поле для даты удаления
    deleted = models.BooleanField(
        default=False, verbose_name="Удалена"
    )  # Поле для отметки удаления
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Категория",
    )  # Связь с моделью Category, on_delete=models.SET_NULL - при удалении категории связь с ней у задач устанавливается в NULL
    priority = models.ForeignKey(
        Priority,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Приоритет",
    )  # Связь с моделью Priority, on_delete=models.SET_NULL - при удалении приоритета связь с ним у задач устанавливается в NULL

    def __str__(self):  # Метод для отображения названия задачи
        return self.title

    class Meta:  # Метаданные модели
        verbose_name = "Задача"  # Название модели в единственном числе
        verbose_name_plural = "Задачи"  # Название модели во множественном числе
