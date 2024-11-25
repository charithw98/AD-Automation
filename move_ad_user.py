import os
from ldap3 import Server, Connection, ALL, MODIFY_REPLACE
from ldap3.core.exceptions import LDAPException

# Environment variables for security
AD_SERVER = os.getenv('AD_SERVER', 'your_ad_server')
AD_USER = os.getenv('AD_USER', 'your_ad_username')
AD_PASSWORD = os.getenv('AD_PASSWORD', 'your_ad_password')
USER_DN = os.getenv('USER_DN')  # Distinguished Name of the user to move
TARGET_OU = os.getenv('TARGET_OU')  # Target OU to move the user to

def move_user():
    try:
        # Connect to the AD server
        server = Server(AD_SERVER, get_info=ALL)
        conn = Connection(server, AD_USER, AD_PASSWORD, auto_bind=True)

        if not conn.bind():
            print('Failed to bind to the server')
            return

        # Move the user to the target OU
        new_dn = f'CN={USER_DN.split(",")[0][3:]},{TARGET_OU}'
        conn.modify_dn(USER_DN, new_dn)

        if conn.result['description'] == 'success':
            print(f'User {USER_DN} moved successfully to {TARGET_OU}')
        else:
            print(f'Failed to move user: {conn.result}')

        conn.unbind()

    except LDAPException as e:
        print(f'LDAP error: {e}')

if __name__ == '__main__':
    move_user()
