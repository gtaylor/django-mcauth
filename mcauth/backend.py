"""
Minecraft authentication backend.
"""
import logging
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
from django.conf import settings
from mcauth import protocol as mc_protocol

logger = logging.getLogger('mcauth.backend')

class MinecraftAuthServerBackend(ModelBackend):
    """
    A backend that will check the Minecraft auth server to see if the provided
    user/pass is a valid Minecraft account. Will create the account
    """
    def authenticate(self, username=None, password=None):
        try:
            # Successful authentication returns the case-correct username
            # from the Minecraft auth servers. Invalid user/pass results in
            # a False value.
            username_case = mc_protocol.auth_against_mcserver(username,
                                                              password)
        except mc_protocol.MinecraftAuthServerException:
            logger.error("Minecraft auth server error while trying "\
                         "to authenticate %s" % username)
            return None

        # This will be False if the authentication was unsuccessful.
        if username_case:
            if self._create_unknown_user():
                # Unknown users are created upon authentication.
                user, created = User.objects.get_or_create(
                                    username=username_case)
                return user
            else:
                # Don't create new User objects.
                try:
                    return User.objects.get(username=username_case)
                except User.DoesNotExist:
                    # Fall through to None at end.
                    pass

        # Invalid user/pass.
        logger.warning("Failed login attempt for %s" % username)
        return None

    def _create_unknown_user(self):
        """
        Checks settings to see if any users that successfully authenticate, but
        don't already exist locally should be created.

        :rtype: bool
        :returns: True if new User objects should be created upon all
            successful authentications.
        """
        return getattr(settings, 'MCAUTH_CREATE_UNKNOWN_USERS', True)