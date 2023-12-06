from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json

class SimpleRequestHandler(BaseHTTPRequestHandler):
    data_store = []

    def do_GET(self):
        # Gérer la route /get
        if self.path == '/get':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            # Renvoyer les données stockées sous forme de JSON
            response_data = {'data': self.data_store}
            self.wfile.write(json.dumps(response_data).encode('utf-8'))
        else:
            # Si la route n'est pas reconnue, renvoyer une réponse 404
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        # Gérer la route /add
        if self.path == '/add':
            # Récupérer la longueur du contenu du message
            content_length = int(self.headers['Content-Length'])
            # Lire le corps du message POST
            post_data = self.rfile.read(content_length)
            # Parser les données JSON
            data = json.loads(post_data.decode('utf-8'))

            # Ajouter les données à la mémoire
            self.data_store.append(data)

            # Renvoyer une réponse 200 OK
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response_data = {'message': 'Données ajoutées avec succès'}
            self.wfile.write(json.dumps(response_data).encode('utf-8'))
        else:
            # Si la route n'est pas reconnue, renvoyer une réponse 404
            self.send_response(404)
            self.end_headers()

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleRequestHandler)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
