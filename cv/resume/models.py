import os
from django.db import models
from django.utils import timezone

# Create your models here.
class Skill(models.Model):

    # skills information
    logo = models.ImageField("Logo_Image")
    name = models.CharField("name", max_length=15)
    level = models.CharField("level", max_length=50)
    
    
    def __str__(self):
        return f" [{self.name}]"
    
def project_media_upload(instance, filename):
    # Get the project name and remove any special characters or spaces
    project_name = instance.name
    project_name = ''.join(e for e in project_name if e.isalnum())

    # Determine if the uploaded file is an image or a video
    file_extension = os.path.splitext(filename)[1].lower()
    if file_extension in ('.jpg', '.jpeg', '.png', '.gif'):
        media_type = 'images'
    elif file_extension in ('.mp4', '.avi', '.mov'):
        media_type = 'videos'
    else:
        media_type = 'other'

    # Generate the path for the media
    path = f"project_media/{project_name}/{media_type}/{filename}"

    return path
    
class Project(models.Model):
    name = models.CharField(max_length=255)
    image1 = models.ImageField(upload_to=project_media_upload)
    image2 = models.ImageField(upload_to=project_media_upload)
    image3 = models.ImageField(upload_to=project_media_upload)
    image4 = models.ImageField(upload_to=project_media_upload)
    video = models.FileField(upload_to=project_media_upload)
    skills = models.CharField(max_length=1000)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name} - {self.subject}'
    
