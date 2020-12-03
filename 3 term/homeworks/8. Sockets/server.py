import socket
import re 

from protocol import recv_with_size, send_with_size


EMAIL_REGEX = r'[\w\.-]+@[\w\.-]+\.\w+'

def find_emails(string):
    return "\n".join(set(re.findall(EMAIL_REGEX, string)))


def run_server(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.bind((host, port))
    sock.listen()
    print("The server is running...")
    
    while True:
        conn, addr = sock.accept()
        print("Connect from {}".format(addr))

        try:
            input_data = recv_with_size(conn, 1024).decode("utf-8")
            emails = find_emails(input_data)
            send_with_size(conn, emails.encode())
            print("Requst handled")
        except socket.error as e:
            print(e)
        finally:
            conn.close()
            print("Close connection with {}\n".format(addr))


if __name__ == '__main__':
    run_server('', 9094)
