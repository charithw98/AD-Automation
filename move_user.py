from ldap3 import Server, Connection, ALL, MODIFY_REPLACE
import sys

def move_user(ad_username, target_ou, server_ip, ad_user, ad_password):
    try:
        # Connect to the AD server
        server = Server(server_ip, get_info=ALL)
        conn = Connection(server, user=f"{ad_user}@test.com", password=ad_password, auto_bind=True)


        # Define the user's DN and the target OU DN
        user_dn = f"CN={ad_username},OU=TestOU2,DC=example,DC=com"  # Adjust based on your environment
        target_dn = f"OU={target_ou},DC=example,DC=com"

        # Prepare the move operation
        move_result = conn.modify_dn(user_dn, target_dn)
        
        if move_result:
            print(f"Successfully moved user {ad_username} to {target_ou}")
        else:
            print(f"Failed to move user {ad_username}: {conn.last_error}")
            sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: move_user.py <username> <target_ou> <server_ip> <ad_user> <ad_password>")
        sys.exit(1)

    username = sys.argv[1]
    target_ou = sys.argv[2]
    server_ip = sys.argv[3]
    ad_user = sys.argv[4]
    ad_password = sys.argv[5]

    move_user(username, target_ou, server_ip, ad_user, ad_password)
