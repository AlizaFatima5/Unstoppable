import os
from daphne import server
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BookYourBarber.settings")

application = get_asgi_application()

if __name__ == "__main__":
    server.run("BookYourBarber.asgi:application", port=8000, host="0.0.0.0")
