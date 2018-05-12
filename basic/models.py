from django.db import models
from django.utils import timezone


# Create your models here.

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    soft_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def create_blog(self, data):
        blog_created = True
        try:
            Blog.objects.create(title=data['title'], description=data['description'])
        except Exception as ex:
            print(ex)
            blog_created = False
        return blog_created

    def update_blog(self, data):
        blog_updated = True
        try:
            updated = Blog.objects.filter(id=data['id']
                                          ).update(title=data['title'],
                                                   description=data['description'],
                                                   updated_at=timezone.now()
                                                   )
            if not updated:
                blog_updated = False
        except Exception as ex:
            print(ex)
            blog_updated = False
        return blog_updated

    def delete_blog(self, blog_id):
        blog_deleted = True
        try:
            deleted = Blog.objects.filter(id=blog_id).update(soft_delete=True,
                                                                updated_at=timezone.now())
            if not deleted:
                blog_deleted = False
        except Exception as ex:
            print(ex)
            blog_deleted = False
        return blog_deleted

    def get_active_blogs(self):
        active_blogs = []
        try:
            active_blogs = Blog.objects.filter(soft_delete=False).values('id', 'title', 'description', 'created_at')
            active_blogs = list(active_blogs)
        except Exception as ex:
            print(ex)
        return active_blogs

    def get_blog(self, blog_id):
        blog = {}
        try:
            blog = Blog
        except Exception as ex:
            print(ex)
        return blog

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blogs'
