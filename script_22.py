import os

for key, value in os.environ.items():
    print(key, ':', value)
# LANG : en_IN
# USER : swadhi
# HOME : /home/swadhi
# ...

""" User defined environment variable """
temp_env_dict = {'user': 'user@facebook.com', 'pwd': 'secret' }

# Update environment variable temporarily
os.environ.update( temp_env_dict )

# Access environment variable that was set earlier
username, password = os.environ['user'], os.environ['pwd']

print('Logging in with credentials: ({}:{}) ...'.format(username, password))
# Logging in with credentials: (user@facebook.com:secret) ...
