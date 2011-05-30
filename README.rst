django-mcauth
=============

django-mcauth is a pluggable authentication back-end that lets your users
login with their Minecraft.net user/pass.

.. warning:: Authentication against Minecraft.net auth servers is not
    officially endorsed, and may cease to work at any time. Using a fallback
    authentication backend (like Django's default) will prevent complete
    failure if Notch ever decides to lock things down. Also keep in mind that
    if you run a high traffic site, you may be asked to stop hitting the
    Minecraft.net auth server.

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

If you have questions or ideas, or encounter bugs, add an entry to our
`issue tracker`_.

.. _issue tracker: https://github.com/gtaylor/django-mcauth/issues
  
License
-------

django-mcauth is licensed under the `BSD License`_.

.. _BSD License: https://github.com/gtaylor/django-mcauth/blob/master/LICENSE
