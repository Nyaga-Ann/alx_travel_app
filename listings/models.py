from django.db import models

class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    location = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Booking(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=100)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"{self.guest_name} - {self.listing}"


class Review(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.reviewer_name} - {self.rating}/5"
