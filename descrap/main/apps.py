from django.apps import AppConfig
import os
from datetime import datetime

class MainConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "main"

def user_directory_path(instance,filename):
    date = datetime.now()
    name= date.strftime('%H:%M')
    path = "images/"
    extension = "." + filename.split('.')[-1]

    # Filename reformat
    filename_reformat = 'scrap' +name + extension

    return os.path.join(path, filename_reformat)