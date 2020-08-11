from django.db import models


# Create your models here.
class Bbs_data(models.Model):
    # name = models.CharField(max_length=50)
    # descript = models.TextField()
    # price = models.FloatField()
    # quantity = models.IntegerField()
    # cdate = models.DateTimeField(auto_now_add=True)

    postnum = models.IntegerField()
    posttitle = models.CharField(max_length=200)
    post = models.CharField(max_length=500)
    writer = models.CharField(max_length=50)
    createdtime = models.DateTimeField()
    nowtime = models.TimeField()

    def __str__(self):
        return 'id : {},name : {},description : {}'.format(self.id, self.name, self.descript)
