# Configuration file for Jupyter Hub

c = get_config()

# spawn with Docker
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.container_image = 'singleuser'
c.DockerSpawner.extra_create_kwargs.update({ 'ports': {'%i/tcp' % 4040: None} })
# The docker instances need access to the Hub, so the default loopback port doesn't work:
from jupyter_client.localinterfaces import public_ips
c.JupyterHub.hub_ip = public_ips()[0]
c.JupyterHub.port = 443
c.DockerSpawner.extra_host_kwargs.update({ 'port_bindings': {'%i/tcp' % 4040: (public_ips()[0],) }})

#c.JupyterHub.proxy_cmd = ['configurable-http-proxy', '--redirect-port', '80']

# OAuth with GitHub
import os
c.JupyterHub.authenticator_class = 'oauthenticator.GitHubOAuthenticator'
c.GitHubOAuthenticator.oauth_callback_url = os.environ['OAUTH_CALLBACK_URL']

c.Authenticator.whitelist = whitelist = {'menshawi'}
c.Authenticator.admin_users = admin = {'menshawi'}

c.JupyterHub.admin_access = True

# import os

# join = os.path.join
# here = os.path.dirname(__file__)
# with open(join(here, 'userlist')) as f:
#     for line in f:
#         if not line:
#             continue
#         parts = line.split()
#         name = parts[0]
#         whitelist.add(name)
#         if len(parts) > 1 and parts[1] == 'admin':
#             admin.add(name)

#c.GitHubOAuthenticator.oauth_callback_url = os.environ['OAUTH_CALLBACK_URL']

# ssl config
# ssl = join(here, 'ssl')
# keyfile = join(ssl, 'ssl.key')
# certfile = join(ssl, 'ssl.crt')
# if os.path.exists(keyfile):
#     c.JupyterHub.ssl_key = keyfile
# if os.path.exists(certfile):
#     c.JupyterHub.ssl_cert = certfile
#     c.JupyterHub.port = 443
