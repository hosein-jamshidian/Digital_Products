from django.db import models
from django.utils.translation import ugettext_lazy as _

class Product(models.Model):
    title=models.CharField(_("title"),max_length=50)
    description=models.TextField(_("description"),blank=True)
    avatar=models.ImageField(_("avatar"),blank=True,upload_to="products/")
    is_enable=models.BooleanField(_("is_enable"),default=True)
    create_time=models.DateTimeField(_("create_time"),auto_now_add=True)
    uploaded_time=models.DateTimeField(_("uploaded_time"),auto_now_add=True)
    categories=models.ManyToManyField("Category",verbose_name=_("category"),blank=True)

    class Meta:
        db_table="products"
        verbose_name=_("Product")
        verbose_name_plural=_("Products")
    def __str__(self):
        return self.title

class Category(models.Model):
    parent=models.ForeignKey("self",verbose_name=_("parent"),blank=True,null=True,on_delete=models.CASCADE)
    title = models.CharField(_("title"), max_length=50)
    description = models.TextField(_("description"), blank=True)
    avatar = models.ImageField(_("avatar"), blank=True, upload_to="categories/")
    is_enable = models.BooleanField(_("is_enable"), default=True)
    create_time = models.DateTimeField(_("create_time"), auto_now_add=True)
    uploaded_time = models.DateTimeField(_("uploaded_time"), auto_now_add=True)

    class Meta:
        db_table = "categories"
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
    def __str__(self):
        return self.title

class File(models.Model):
    FILE_AUDIO=1
    FILE_VIDEO=2
    FILE_PDF=3
    FILE_TYPES=(
        (FILE_AUDIO,_("audio")),
        (FILE_VIDEO,_("video")),
        (FILE_PDF,_("pdf"))
    )
    product=models.ForeignKey("Product",verbose_name=_("product"),related_name="files",on_delete=models.CASCADE)
    title = models.CharField(_("title"), max_length=50)
    file=models.FileField(_("file"),upload_to="files/%Y/%m/%d/")
    is_enable = models.BooleanField(_("is_enable"), default=True)
    file_type=models.PositiveSmallIntegerField(_("file type"),default=1,choices=FILE_TYPES)
    create_time = models.DateTimeField(_("create_time"), auto_now_add=True)
    uploaded_time = models.DateTimeField(_("uploaded_time"), auto_now_add=True)
    class Meta:
        db_table = "files"
        verbose_name = _("File")
        verbose_name_plural = _("Files")
    def __str__(self):
        return self.title