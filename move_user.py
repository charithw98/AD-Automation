from ldap3 import Server, Connection, ALL
import sys

def test_login(server_ip, ad_user, ad_password):
    try:
        # Connect to the AD server
        server = Server(server_ip, get_info=ALL)
        conn = Connection(server, user=f"CN={ad_user},CN=Users,DC=test,DC=com", password=ad_password, auto_bind=True)

        if conn.bind():
            print("Successfully connected to the AD server.")
            conn.unbind()  # Close the connection
        else:
            print(f"Failed to connect to the AD server: {conn.result}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: test_login.py <server_ip> <ad_user> <ad_password>")
        sys.exit(1)

    server_ip = sys.argv[1]
    ad_user = sys.argv[2]
    ad_password = sys.argv[3]

    test_login(server_ip, ad_user, ad_password)
