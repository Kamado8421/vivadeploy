from django.db import models
from django.contrib.auth.models import User

class InfoUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField(blank=True, null=True, max_length=200, default="<Vazio>")
    birth = models.DateField(blank=True, null=True)
    url_profile = models.URLField(blank=True, null=True, default="https://cdn-icons-png.flaticon.com/512/3106/3106807.png")
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    quant_posts = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} - {self.biography}'


class CategoryPost(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title

class Publication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_publicate = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    legend = models.TextField(blank=True, null=True, max_length=100, default="")
    url_img = models.URLField(blank=False, null=False)
    tag_category = models.ForeignKey(CategoryPost, on_delete=models.CASCADE, blank=True, null=True)
    users_interactions = models.ManyToManyField(User, related_name='publications_interacted', blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.date_publicate}'