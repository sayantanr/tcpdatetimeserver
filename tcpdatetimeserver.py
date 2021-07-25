import socketserver
from datetime import datetime

class DateHandler(socketserver.StreamRequestHandler):
    def handle(self):
        self.wfile.write(f'{datetime.now().isoformat()}\n'.encode('utf-8'))

with socketserver.TCPServer(('', 59090), DateHandler) as server:
    print('The date server is running...')
    server.serve_forever()
