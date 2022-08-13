from django.db import models

# class Visitor(models.Model):
#     """A Visitor is an user who has logged in."""
#     # visitor_id = models.BigIntegerField(help_text="") # use the default pk
#     name = models.CharField(max_length=40,help_text="Visitor name.")
#     email = models.EmailField(help_text="Visitor email.")
#     # created_time = models.DateTimeField(help_text="Visitor created time.")
#     created_time = models.DateField(help_text="Visitor created time.")
#
#     def __str__(self):
#         return "Visitor name: {} | Visitor email: {}".format(self.name, self.email)


class ShortURL(models.Model):
    url_key = models.CharField(max_length=7, unique=True, help_text="The shortened URL.")
    original_url = models.URLField(help_text="The original URL.")
    user_id = models.BigIntegerField(unique=False, null = True, help_text="User ID")
    created_time = models.DateField(null=True, help_text="The Short URL created time.")

    def __str__(self):
        return "Shortened URL: {}".format(self.url_key)

