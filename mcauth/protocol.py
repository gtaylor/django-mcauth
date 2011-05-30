import socket
import urllib2

class MinecraftAuthServerException(Exception):
    """
    Raise this when the Minecraft auth server is unresponsive or unavailable.
    """
    def __str__(self):
        return "The Minecraft auth server is not available at this time."

def auth_against_mcserver(username, password, timeout=7.0):
    """
    :param str user: The username to attempt to authenticate with.
    :param str password: The password for the given username.

    :rtype: str or bool
    :returns: If authentication is successful, returns the case-correct
        username. If it fails, returns False.
    :raises: MinecraftAuthServerException on auth server failure.
    """
    auth_url = 'https://login.minecraft.net/?user=%s&password=%s&version=99999' % (
        username, password,
    )

    socket.setdefaulttimeout(timeout)
    try:
        response = urllib2.urlopen(auth_url)
    except urllib2.URLError:
        # Something bad happened to the auth server.
        raise MinecraftAuthServerException

    result = response.read()

    if result.startswith('Bad login'):
        return False

    game_version, dl_ticket, username_case, session_id = result.split(':')

    return username_case
