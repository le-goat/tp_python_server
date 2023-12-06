from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleRequestHandler(BaseHTTPRequestHandler):
    data_store = []
    iterator = 0

    def do_GET(self):
        if self.path == '/health':
            # Route /health
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response_data = {'status': 'OK'}
            self.wfile.write(json.dumps(response_data).encode('utf-8'))
        elif self.path == '/get':
            # Route /get
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response_data = {'status': 'OK', 'iterator': self.iterator}
            self.wfile.write(json.dumps(response_data).encode('utf-8'))
        else:
            # Route non reconnue
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == '/add':
            # Route /add
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))

            # Vérifier que la clé 'value' est présente
            if 'value' in data and isinstance(data['value'], int):
                # Mettre à jour l'itérateur
                self.iterator += data['value']
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response_data = {'status': 'OK', 'message': 'Iterator value updated successfully'}
                self.wfile.write(json.dumps(response_data).encode('utf-8'))
            else:
                # Erreur si la clé 'value' n'est pas présente ou n'est pas un entier
                self.send_response(400)
                self.end_headers()
        else:
            # Route non reconnue
            self.send_response(404)
            self.end_headers()


def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleRequestHandler)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()


if __name__ == '__main__':
    run_server()
