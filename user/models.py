from django.db import models

# Create your models here.
class contactus(models.Model):
    Name=models.CharField(max_length=50)
    Mobile=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Message=models.TextField()
    def __str__(self):
        return self.Name

class category(models.Model):
    Name=models.CharField(max_length=20)
    CPic=models.ImageField(upload_to='static/category/',default="")
    def __str__(self):
        return self.Name

###########################################################

###########################################################
class maincate(models.Model):
    Name = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='static/mcategory/')
    cdate = models.DateField()

    def __str__(self):
        return self.Name


###########################################################
class myproduct(models.Model):
    pprice=models.FloatField()
    dprice=models.FloatField()
    psize=models.CharField(max_length=20)
    pcolor=models.CharField(max_length=20)
    pdes=models.TextField()
    pdel=models.CharField(max_length=50)
    ppic=models.ImageField(upload_to='static/product/',default="")
    pdate=models.DateTimeField()
    pcategory=models.ForeignKey(category,on_delete=models.CASCADE,null=True)
    mcategory=models.ForeignKey(maincate,on_delete=models.CASCADE,null=True)

class morder(models.Model):
    userid=models.CharField(max_length=70)
    pid=models.IntegerField()
    remarks=models.CharField(max_length=20)
    odate=models.CharField(max_length=30)
    status=models.BooleanField()

class mcart(models.Model):
    userid=models.CharField(max_length=70)
    pid=models.IntegerField()
    cdate=models.CharField(max_length=100)
    status=models.BooleanField()
class  uregister(models.Model):
    name=models.CharField(max_length=20)
    mobile=models.CharField(max_length=20)
    email=models.CharField(max_length=50,primary_key=True)
    passwd=models.CharField(max_length=30,null=True)
    userpic=models.ImageField(upload_to='static/uregister/',default="")
    message=models.CharField(max_length=400)