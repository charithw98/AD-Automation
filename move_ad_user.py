from ldap3 import Server, Connection, ALL
import os
import sys

# Environment variables passed from Jenkins
ad_server = os.getenv('AD_SERVER')
ad_user = os.getenv('AD_USER')
ad_password = os.getenv('AD_PASSWORD')
username = os.getenv('USERNAME')   # User to move
destination_ou = os.getenv('DESTINATION_OU')  # Selected OU

# Construct Distinguished Names (DN)
user_dn = f'CN={username},OU=TestOU1,DC=example,DC=com'  # Modify according to your structure

try:
    # Connect to AD server
    server = Server(ad_server, get_info=ALL)
    conn = Connection(server, ad_user, ad_password, auto_bind=True)

    # Move user to the destination OU
    conn.modify_dn(user_dn, f'CN={username}', new_superior=destination_ou)

    # Check result
    if conn.result['description'] == 'success':
        print(f"User {username} moved to {destination_ou} successfully.")
    else:
        print(f"Failed to move user: {conn.result['description']}")
except Exception as e:
    print("Error:", str(e))
