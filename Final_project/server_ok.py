import termcolor
import http.server
import socketserver
import Functions as f
PORT = 8080
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, 'blue')
        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happy server: It always returns a message saying
        # that everything is ok
        if self.path == "/":
            contents = f.read_html_file("./html/main_page.html")
        elif self.path == "/info/A":
            contents = f.read_html_file("./html/main_page.html")
        elif self.path == "/info/C":
            contents = f.read_html_file("./html/info/C.html")
        elif self.path == "/info/G":
            contents = f.read_html_file("./html/info/G.html")
        elif self.path == "/info/T":
            contents = f.read_html_file("./html/info/T.html")
        elif self.path.endswith((".html")):
            try:
                contents = f.read_template_html_file(".html" + self.path)
            except FileNotFoundError:
                contents = f.read_template_html_file("html/Error.html")
        else:
            contents = f.read_template_html_file("html/Error.html")
        # Message to send back to the clinet


        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html' )
        self.send_header('Content-Length', len(str(contents).encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()