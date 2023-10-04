from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model
User = get_user_model()
class Advertisement(models.Model):
    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("Торг", help_text="Отметьте, если торг уместен")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete= models.CASCADE, null=True)
    image = models.ImageField('изображения', upload_to="advertisements")

    @admin.display(description = 'дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                 f'<span style = "color: green; font-weight: bold;">Сегодня в {created_time}</span>'
            )
        return self.created_at.strftime("%d.%m.%Y в '%H:%M:%S")
    class Meta:
        db_table = "advertisements"
    def __str__(self):
        return f"Advertisement(id={self.id}, tirle={self.title}, price={self.price}"

    @admin.display(description='дата обновления')
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime('%H:%M:%S')
            return format_html(
                f'<span style = "color: blue; font-weight: bold;">Сегодня в {updated_time}</span>'
            )

    @admin.display(description='фото')
    def get_html_image(self):
        if self.image:
            return format_html(
                '<img src="{url}" style="max-width: 80px; max-height: 80px;"', url=self.image.url
            )

