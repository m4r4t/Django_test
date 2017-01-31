from __future__ import unicode_literals

SECRET_KEY = "b495a05c396843b6b47ac944a72c92ed"
NEVERCACHE_KEY = "b5d87bb4e17c483093296fa321056bdc"
ALLOWED_HOSTS = ["192.168.33.20.xip.io",]

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        # DB name or path to database file if using sqlite3.
        "NAME": "djangotestdb",
        # Not used with sqlite3.
        "USER": "djangotestuser",
        # Not used with sqlite3.
        "PASSWORD": "p4ccW0rd",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "127.0.0.1",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")

CACHE_MIDDLEWARE_SECONDS = 60

CACHE_MIDDLEWARE_KEY_PREFIX = "djangotest"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "LOCATION": "127.0.0.1:11211",
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
STATIC_ROOT="./static"
