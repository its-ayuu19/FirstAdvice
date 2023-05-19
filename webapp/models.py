
from django.db import models

def generate_key_doctor():
    key = None
    try:
        print("try")
        key = DoctorKey.objects.all()[0]
    except IndexError:
        print("except")
        key = DoctorKey()

    print(key)
    value = int(key.key)
    key.key = value + 1
    key.save()
    return value

class DoctorKey(models.Model):
    key = models.IntegerField(default=1)

class Disease(models.Model):
    disease = models.CharField(primary_key = True,max_length=50)
    specialization = models.CharField(max_length=100)

class Doctor(models.Model):
    id = models.AutoField(primary_key=True, default=generate_key_doctor, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=100)
    education = models.CharField(max_length=200)
    experience = models.IntegerField()
    location = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    positive = models.IntegerField(default=0)
    negative = models.IntegerField(default=0)

    def get_rating(self):
        total = self.positive + self.negative
        if(total == 0):
            return 0
        rating = self.positive / total * 10
        return rating

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kargs):
        super().save(*args, **kargs)

class Patient(models.Model):
    id = models.AutoField(primary_key=True, default=True, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    location = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique = True, max_length=254)
    password = models.CharField(max_length=20)


    def __str__(self):
        return str(self.id)

    def save(self, *args, **kargs):
        super().save(*args, **kargs)