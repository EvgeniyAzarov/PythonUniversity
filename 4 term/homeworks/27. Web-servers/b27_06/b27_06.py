from http.server import HTTPServer, CGIHTTPRequestHandler

HOST = ""
PORT = 8001

if __name__ == '__main__':
    print("Server started")
    HTTPServer((HOST, PORT), CGIHTTPRequestHandler).serve_forever()
