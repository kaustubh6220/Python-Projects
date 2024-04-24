# from django.db import models

# # Create your models here.
# # models.py
# from django.contrib.auth.models import User
# from django.db import models

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # Add any additional fields you need for the user profile
#     # For example:
#     # bio = models.TextField(blank=True)

# class Seat(models.Model):
#     row = models.IntegerField()
#     column = models.IntegerField()
#     status = models.CharField(max_length=20)  # 'available', 'reserved', 'occupied', etc.

#     def __str__(self):
#         return f"Seat {self.row}-{self.column}: {self.status}"