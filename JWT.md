to send JSON data between systems.
mostly information about users for authentication and etc.
popular when users need to interact with multiple back-end servers.

dot separated parts of JWT:

header (b64)
payload (b64); contains claims about a user
signature; encrypted hash of the header and the payload