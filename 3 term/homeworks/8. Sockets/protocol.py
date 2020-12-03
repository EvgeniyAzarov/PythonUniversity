import socket
import sys
import struct

def recv_with_size(sock, buff_size):
    total_data = [] 
    total_len = 0
    size = sys.maxsize
    # First 4 byte of message, which should say 
    # how long message is
    size_data = b"" 
   
    while total_len < size:
        buff = sock.recv(buff_size)
        if total_data:
            total_data.append(buff)
            total_len += len(buff)
        else: 
            if len(buff) > 4:
                size_data += buff
                size = struct.unpack('>i', size_data[:4])[0]
                total_data.append(size_data[4:])
                total_len += len(size_data[4:])
            else:
                size_data += buff

    return b"".join(total_data)
            

def send_with_size(sock, data):
    sock.sendall(struct.pack('>i', len(data)) + data)
