import socket

from protocol import recv_with_size, send_with_size


if __name__ == '__main__':
    f = open("test_conversation.txt")
    data = "\n".join(f.readlines())    
    f.close()
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 9094))  
    
    send_with_size(sock, data.encode())
    emails = recv_with_size(sock, 1024).decode("utf-8")
    print(emails)

    sock.close()
