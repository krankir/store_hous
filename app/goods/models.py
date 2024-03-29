from django.db import models


class Categories(models.Model):
    name = models.CharField(
        max_length=150, unique=True, verbose_name='Название'
    )
    slug = models.SlugField(
        max_length=254, unique=True, blank=True, null=True, verbose_name='URL'
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(
        max_length=150, unique=True, verbose_name='Название'
    )
    slug = models.SlugField(
        max_length=254, unique=True, blank=True, null=True, verbose_name='URL'
    )
    description = models.TextField(
        blank=True, null=True, verbose_name='описание'
    )
    image = models.ImageField(
        upload_to='goods_images',
        blank=True,
        null=True,
        verbose_name='изображение'
    )
    price = models.DecimalField(
        default=0.00,
        max_digits=7,
        decimal_places=2,
        verbose_name='цена'
    )
    discount = models.DecimalField(
        default=0.00,
        max_digits=4,
        decimal_places=2,
        verbose_name='скидка %'
    )
    quantity = models.PositiveIntegerField(
        default=0, verbose_name='количество'
    )
    category = models.ForeignKey(
        to=Categories, on_delete=models.CASCADE, verbose_name='категория')

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('id',)

    def __str__(self):
        return f'{self.name} количество - {self.quantity}'

    def display_id(self):
        return f'{self.id:05}'

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount/100, 2)

        return self.price
