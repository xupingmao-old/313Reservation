#!/etc/bin/bash
python manage.py runserver &
google-chrome http://127.0.0.1:8000 &
