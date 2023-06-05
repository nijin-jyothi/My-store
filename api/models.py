from django.db import models

class Products(models.Model):
    name=models.CharField(max_length=50)
    price=models.PositiveIntegerField(default=100)
    category=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Products.objects.create(name="nanpro",price=715,category="healthcare",description="soap")
# Model_name.objects.create(hbfhbafhbfsfbs)
#

# fetch all products
# qs=Products.objects.all()
# qs=Model_name.objects.all()

# fetch one product
# qs=Modelname.objects.get(id=2)
# qs=Products.objects.get(id=3)

# to update
# Products.objects.filter(id=1).update(price=price to update)

# to filter
# Products.objects.filter(category="food")

# to delete
# Products.objects.get(id=3).delete()
