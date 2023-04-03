from django.db import models




class Category(models.Model):
    HOME_CATEGORY = (
        ('Orphaned', 'Orphaned'),
        ('Street', 'Street'),
        ('Special', 'Special')
    )
    #name = models.CharField(max_length=155)
    type = models.CharField(max_length=55, choices=HOME_CATEGORY)
    image = models.ImageField(upload_to="home_media")


    def __str__(self):
        return self.type




class Donor(models.Model):
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    email = models.EmailField()
    address = models.CharField(max_length=155)
    county = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"




class ChildrenHome(models.Model):
    name = models.CharField(max_length=155)
    location = models.CharField(max_length=155)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    county = models.CharField(max_length=155)
    address = models.CharField(max_length=155)
    about_us = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='childrenhomes_media')
    image2 = models.ImageField(upload_to='childrenhomes_media')
    image3 = models.ImageField(upload_to='childrenhomes_media')
    num_children = models.PositiveIntegerField()
    age_group = models.CharField(max_length=255)
    main_challenges = models.TextField()
    activities = models.TextField()


    def __str__(self):
        return self.name
    
class Donations(models.Model):
    DONATION_TYPE = (
        ('anonymous', 'anonymous'),
        ('dedicated', 'dedicated')
    )
    donation_type = models.CharField(max_length=155, choices=DONATION_TYPE)
    message = models.TextField()
    donation_amount = models.CharField(max_length=155)
    donation_date = models.DateField(auto_now=True)
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    home = models.ManyToManyField(ChildrenHome)


    def __str__(self):
        return self.donation_type
    

   
