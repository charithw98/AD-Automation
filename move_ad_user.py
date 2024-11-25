import os
from ldap3 import Server, Connection, ALL

# Load environment variables from Jenkins
ad_server = os.getenv('AD_SERVER')
ad_user = os.getenv('AD_USER')
ad_password = os.getenv('AD_PASSWORD')
username = os.getenv('AD_USERNAME')
destination_ou = os.getenv('DESTINATION_OU')

# Construct the user's distinguished name (DN) assuming standard structure
user_dn = f"CN={username},OU=TestOU1,DC=example,DC=com"

try:
    # Connect to the AD server
    server = Server(ad_server, get_info=ALL)
    conn = Connection(server, ad_user, ad_password, auto_bind=True)

    # Perform the move operation
    conn.modify_dn(user_dn, f'CN={username}', new_superior=destination_ou)
    if conn.result['description'] == 'success':
        print(f"User {username} moved to {destination_ou} successfully.")
    else:
        print("Failed to move user:", conn.result['description'])
except Exception as e:
    print("Error:", str(e))
