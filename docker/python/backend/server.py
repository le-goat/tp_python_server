from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json
import mysql.connector

PORT = 8000

# Config de la connexion au server mysql
db_config = {
    "host": "172.18.0.2",
    "user": "userIterator",
    "password": "qwerty1234",
    "database": "iterator_db",
}


class SimpleRequestHandler(BaseHTTPRequestHandler):
    data_store = []
    iterator = 0

    def run_query(self, query, params=None, fetchall=False):
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute(query, params)
        if fetchall:
            result = cursor.fetchall()
        else:
            result = cursor.fetchone()
        connection.commit()
        connection.close()
        return result

    def do_GET(self):
        if self.path == '/health':
            # Route /health
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response_data = {'status': 'OK'}
            self.wfile.write(json.dumps(response_data).encode('utf-8'))
        elif self.path == '/get':
            query = "SELECT state FROM interator"
            result = self.run_query(query, fetchall=False)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response_data = {'status': 'OK', 'iterator': result}
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
                query = "UPDATE interator SET state = state + %s"
                params = (data['value'],)
                self.run_query(query, params)

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


def run_server(port):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleRequestHandler)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()


if __name__ == '__main__':
    run_server(PORT)
