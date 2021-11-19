import socket, json
# Used to send a request to socket
class InternalSocket():
    def __init__(self):
        self.host = '127.0.0.1'  # The server's hostname or IP address
        self.port = 5073 # The port used by the server
    def send_request(self, username, password):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall("{{\"msg\": \"{m}\", \"username\": \"{u}\", \"password\": \"{p}\"}}"
                      .format(m="Sending username & password", u=username, p=password).encode())
            data = s.recv(1024)
            data = json.loads(data.decode())
            if "successfully" in data["response"]:
                return True
        return False