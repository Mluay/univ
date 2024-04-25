from django.db import models

class City(models.Model):
    cid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class University(models.Model):
    CHOICES = [
        ('p','اهلية'),
        ('g','حكومية')
    ]
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='universities')
    utype = models.CharField(max_length=10, choices=CHOICES)
    def __str__(self):
        return self.name

class College(models.Model):
    cid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class UniversityCollege(models.Model):
    
    collage = models.ForeignKey(College, on_delete=models.PROTECT)
    university = models.ForeignKey(University, on_delete=models.PROTECT, related_name='colleges')
    def __str__(self):
        return str(self.collage) + ' - ' + str(self.university)


class Hobby(models.Model):
    hid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Department(models.Model):
    CHOICES = [
        ('s','علمي'),
        ('l','ادبي'),
        ('b','علمي و ادبي'),
    ]

    did = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    college = models.ForeignKey(UniversityCollege, on_delete=models.PROTECT, related_name='departments')
    hobbies = models.ManyToManyField(Hobby)
    dtype = models.CharField(max_length=10, choices=CHOICES, null=True)
    min_avg = models.FloatField(null=True)
    def __str__(self):
        return self.name + ' - ' + str(self.college)


class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='post_images/')
    content = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title