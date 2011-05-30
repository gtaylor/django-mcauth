django-mcauth
=============

django-mcauth is a pluggable authentication back-end that lets your users
login with their Minecraft.net user/pass.

Requirements
------------

* Django 1.2+
* Python 2.6 or 2.7 (I don't care to officially support 2.5)

Installation
------------

Add ``'mcauth.backend.MinecraftAuthServerBackend'`` to your settings.py like
so::

    AUTHENTICATION_BACKENDS = (
        'mcauth.backend.MinecraftAuthServerBackend',
        'django.contrib.auth.backends.ModelBackend',
    )

If you don't want to create new local Django users when someone logs in with
a valid user/pass, but doesn't already exist in the DB, you can do this in
settings.py::

    # Only existing User objects can be authenticated against.
    MCAUTH_CREATE_UNKNOWN_USERS = False

Support
-------
  
License
-------

django-mcauth is licensed under the `BSD License`_.

.. _BSD License: https://github.com/gtaylor/django-mcauth/blob/master/LICENSE
