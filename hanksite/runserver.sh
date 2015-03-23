sudo kill -9 $(ps ax | grep 'python manage.py runserver' | awk '{ print $1 }')
# sudo kill -9 $(ps ax | grep 'ipmitool' | awk '{ print $1 }')
sudo python manage.py runserver 0.0.0.0:8000
