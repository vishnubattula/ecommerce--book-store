from django.db import models
from taggit.managers import TaggableManager
from django.core.urlresolvers import reverse
# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=200,db_index=True)
	slug = models.SlugField(max_length=200,db_index=True,unique=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse ('shop:product_list_by_category',args =[self.slug])

class Product(models.Model):
	SKU = models.CharField(max_length=10,)
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True)
	description = models.TextField(blank=True)
	stock = models.PositiveIntegerField()
	sale_price = models.DecimalField(max_digits=10, decimal_places=2)
	regular_price = models.DecimalField(max_digits=10, decimal_places=2)
	category = models.ForeignKey(Category,related_name='products')
	#image = models.CharField(max_length=500,blank=True)
	image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	
	tags = TaggableManager()
	class Meta:
		ordering = ('name',)
		index_together = (('id', 'slug'),)
	
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse ('shop:product_detail',args=[self.id,self.slug])