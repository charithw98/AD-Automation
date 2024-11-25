from ldap3 import Server, Connection, ALL, MODIFY_REPLACE
import os

# Load environment variables
ad_server = os.getenv('AD_SERVER')
ad_user = os.getenv('AD_USER')
ad_password = os.getenv('AD_PASSWORD')
user_dn = os.getenv('USER_DN')
target_ou = os.getenv('TARGET_OU')

try:
    # Connect to the AD server
    server = Server(ad_server, get_info=ALL)
    conn = Connection(server, ad_user, ad_password, auto_bind=True)

    # Perform the move operation
    conn.modify_dn(user_dn, f'CN={user_dn.split(",")[0].split("=")[1]}', new_superior=target_ou)
    if conn.result['description'] == 'success':
        print("User moved successfully.")
    else:
        print("Failed to move user:", conn.result['description'])
except Exception as e:
    print("Error:", str(e))
