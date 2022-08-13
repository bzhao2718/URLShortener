
from .models import ShortURL
import datetime

def save_shorturl(original_url, url_key, user_id=None, visitor=None):
    create_date = datetime.datetime.now()
    shorturl = ShortURL(url_key=url_key, original_url=original_url, created_time=create_date)
    if user_id:
        shorturl.user_id=user_id
    shorturl.save()

def is_key_unique(url_key):
    shorturl = ShortURL.objects.filter(url_key=url_key)
    if shorturl:
        return True
    else:
        return False

def is_url_key_exsits(url_key):
    shorturl = ShortURL.objects.filter(url_key=url_key)
    if shorturl:
        return True
    else:
        return False