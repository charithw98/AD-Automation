# move_ad_user.py
import ldap3
import sys

# Parameters from Jenkins
username = sys.argv[1]
target_ou = sys.argv[2]

# AD Server details
AD_SERVER = 'ldap://<Windows_Server_IP>'
AD_USER = 'tase@test.com'
AD_PASSWORD = 'Testuser@123'

# Connect to AD server
server = ldap3.Server(AD_SERVER)
conn = ldap3.Connection(server, AD_USER, AD_PASSWORD, auto_bind=True)

# Distinguished Name (DN) of the user and target OU
user_dn = f'CN={username},OU=TestOU1,DC=test,DC=com'  # Adjust as per your OU structure
target_dn = target_ou

# Move user
if conn.modify_dn(user_dn, f'CN={username}', new_superior=target_dn):
    print(f'User {username} moved to {target_ou} successfully.')
else:
    print('Failed to move user:', conn.result['description'])

conn.unbind()

