# your_app/settings.py
import os
from UEECnotes.settings import BASE_DIR

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'game/static'),
]
