to send JSON data between systems.
mostly information about users for authentication and etc.
popular when users need to interact with multiple back-end servers.

dot separated parts of JWT:
  -  header (b64)
  -  payload (b64); contains claims about a user
  -  signature; encrypted hash of the header and the payload

# attack

sending a malicious JWT to the server to bypass authentication and access control.

exploiting the flawed JWT handling in the application; e.g. signature verification and then whether it haven't been forged.