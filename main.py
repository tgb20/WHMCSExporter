from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

hostName = "localhost"
serverPort = 4829

API_URL = "https://whmcs.yourwebsite.com/includes/api.php"

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):

        if self.path == "/favicon.ico":
            self.send_response(404)
            return

        payload = {'action': 'GetStats',
                   'username': 'KEY',
                   'password': 'SECRET',
                   'responsetype': 'json'}

        response = requests.request("POST", API_URL, data=payload)

        whmcs = response.json()
        exporter_text = ""

        if whmcs["result"] == "success":
            for key in whmcs:
                if key != "result":
                    data = whmcs[key]
                    if isinstance(data, str):
                        data = data.replace('$', '').replace('USD', '')
                    if isinstance(data, list):
                        data = 0
                    exporter_text += f"# HELP {key} Autogenerated description.\n# TYPE {key} gauge\n{key} {data}\n\n"
        else:
            print(whmcs)
            exporter_text = "failed"

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes(exporter_text, "utf-8"))



if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
