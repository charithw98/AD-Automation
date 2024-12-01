import win32com.client
import sys

def move_user(ad_username, target_ou, server_ip, ad_user, ad_password):
    try:
        # Create the AD connection
        ad = win32com.client.Dispatch("ADODB.Connection")
        connection_string = f"Provider=ADsDSOObject;Data Source=LDAP://{server_ip};"
        ad.Open(connection_string)

        # Authenticate
        ad.Login(ad_user, ad_password)

        # Define the user and the target OU
        user_dn = f"CN={ad_username},OU=TestOU2,DC=example,DC=com"  # Adjust as needed
        target_dn = f"OU={target_ou},DC=example,DC=com"

        # Move user to the target OU
        ad.MoveHere(user_dn, target_dn)
        print(f"Successfully moved user {ad_username} to {target_ou}")
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
