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
    address = models.CharField(max_length=155, blank=True, null=True)
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
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


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
    
class ChildrenHomeDetails(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='children_home_images/')
    num_children = models.PositiveIntegerField()
    age_group = models.CharField(max_length=255)
    main_challenges = models.TextField()
    activities = models.TextField()
    ChildrenHome = models.ForeignKey(ChildrenHome, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
