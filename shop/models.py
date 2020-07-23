from django.db import models


# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="shop/images", default="")
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    zipcode = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    mobile_no = models.IntegerField()

    def __str__(self):
        return self.name

class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc=models.CharField(max_length=5000, default="")
    timestamp=models.DateField(auto_now_add=True)


    def __str__(self):
        return self.update_desc[0:7]+" ..."
