from django.db import models


class Developer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class JSONAPIMeta:
        resource_name = "developers"

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
