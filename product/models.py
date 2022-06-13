# from django.db import models
# from django.db.models import Avg, Count
# from django.urls import reverse
# from django.utils.safestring import mark_safe
# from mptt.fields import TreeForeignKey
# from mptt.models import MPTTModel
#
#
# class Category(MPTTModel):
#     STATUS = (
#         ('True', 'True'),
#         ('False', 'False'),
#     )
#     parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
#     title = models.CharField(max_length=50)
#     keywords = models.CharField(max_length=255)
#     description = models.TextField(max_length=255)
#     image = models.ImageField(blank=True, upload_to='images/')
#     status = models.CharField(max_length=10, choices=STATUS)
#     slug = models.SlugField(null=False, unique=True)
#     create_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.title
#
#     class MPTTMeta:
#         order_insertion_by = ['title']
#
#     def get_absolute_url(self):
#         return reverse('category_detail', kwargs={'slug': self.slug})
#
#     def __str__(self):  # __str__ method elaborated later in
#         full_path = [self.title]  # post.  use __unicode__ in place of
#         k = self.parent
#         while k is not None:
#             full_path.append(k.title)
#             k = k.parent
#         return ' / '.join(full_path[::-1])
#
# # Create your models here.
# class Product(models.Model):
#     STATUS = (
#         ('True', 'True'),
#         ('False', 'False'),
#     )
#
#     VARIANTS = (
#         ('None', 'None'),
#         ('Size', 'Size'),
#         ('Color', 'Color'),
#         ('Size-Color', 'Size-Color'),
#
#     )
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)  # many to one relation with Category
#     title = models.CharField(max_length=150)
#     keywords = models.CharField(max_length=255)
#     description = models.TextField(max_length=255)
#     image = models.ImageField(upload_to='images/', null=False)
#     price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
#     amount = models.IntegerField(default=0)
#     minamount = models.IntegerField(default=3)
#     variant = models.CharField(max_length=10, choices=VARIANTS, default='None')
#     detail = RichTextUploadingField()
#     slug = models.SlugField(null=False, unique=True)
#     status = models.CharField(max_length=10, choices=STATUS)
#     create_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.title
#
#     ## method to create a fake table field in read only mode
#     def image_tag(self):
#         if self.image.url is not None:
#             return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
#         else:
#             return ""
#
#     def get_absolute_url(self):
#         return reverse('category_detail', kwargs={'slug': self.slug})
#
#     def avaregereview(self):
#         reviews = Comment.objects.filter(product=self, status='True').aggregate(avarage=Avg('rate'))
#         avg = 0
#         if reviews["avarage"] is not None:
#             avg = float(reviews["avarage"])
#         return avg
#
#     def countreview(self):
#         reviews = Comment.objects.filter(product=self, status='True').aggregate(count=Count('id'))
#         cnt = 0
#         if reviews["count"] is not None:
#             cnt = int(reviews["count"])
#         return cnt
#
#
# class Images(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     title = models.CharField(max_length=50, blank=True)
#     image = models.ImageField(blank=True, upload_to='images/')
#
#     def __str__(self):
#         return self.title
