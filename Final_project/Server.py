import Functions
import http.server
import socketserver
import termcolor
from urllib.parse import parse_qs
#-------
PORT = 8080
IP = "127.0.0.1"  # localhost

print("The server is ready to connections")
socketserver.TCPServer.allow_reuse_address = True
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
        try:
            if self.path == "/" or self.path == '/main_page.html':
                contents = Functions.read_html_file("./html/main_page.html")
            elif "/limit_sequence" in self.path:
                query_params = self.path.split('?')[1]
                limit = int(parse_qs(query_params)['limit'][0])
                species_len, common_names = Functions.get_info_species(limit)
                format_parameters = {'species_len': species_len, 'limit': limit, 'common_names': common_names}
                contents = Functions.read_template_html_file("./html/limit_sequence.html", **format_parameters)
            #Las dos estrellas estan para simplificar el codigo, y no escribir los keyarguments dos veces,
            #Kwarg => length=length (el primero va en rojo)
            elif "/karyotype" in self.path:
                query_params_kariotype = self.path.split('?')[1]
                name_specie = parse_qs(query_params_kariotype)["karyotype"][0]
                result_karyotype = Functions.get_karyotype(name_specie)
                format_parameters_karyo = {'karyotype': result_karyotype}
                contents = Functions.read_template_html_file("./html/karyotype.html", **format_parameters_karyo)
            elif '/chromosome_length' in self.path:
                query_params_n = self.path.split('?')[1].split('&')[0] #number of chromosome value
                query_params_s = self.path.split('?')[1].split('&')[1] #specie
                specie = parse_qs(query_params_s)['specie'][0]
                number_of_chromosome = int(parse_qs(query_params_n)["length"][0])
                result_number_of_chromosome = str(Functions.get_length_chromosome(specie, number_of_chromosome))
                format_parameter = {'length': result_number_of_chromosome}
                contents = (Functions.read_template_html_file('./html/chromosome_length.html', **format_parameter))
            elif '/gene_seq' in self.path:
                query_params = self.path.split('?')[1]
                name_sequence = parse_qs(query_params)["name"]
                name_sequence = " ".join(name_sequence)
                result_seq, request_name, len_seq, seq_count_A, seq_count_C, seq_count_G, seq_count_T= Functions.get_code_gene_sequence_of_dna(str(name_sequence))
                format_parameter = {'sequence': result_seq}
                contents = Functions.read_template_html_file('./html/gene_seq.html', **format_parameter)
            elif '/gene_info' in self.path:
                query_params = self.path.split('?')[1]
                name_sequence = parse_qs(query_params)["name"]
                name_sequence = " ".join(name_sequence)
                result_seq, request_name, len_seq, seq_count_A, seq_count_C, seq_count_G, seq_count_T = Functions.get_code_gene_sequence_of_dna(str(name_sequence))
                result_start, result_end = Functions.get_start_end(str(name_sequence))
                format_parameter = {'request_name': request_name, 'len_seq': len_seq, 'name_sequence': name_sequence,
                                    'result_start': result_start, 'result_end': result_end}
                contents = Functions.read_template_html_file('./html/gene_info.html', **format_parameter)
            elif '/gene_calculations' in self.path:
                query_params = self.path.split('?')[1]
                name_sequence = parse_qs(query_params)["base"]
                name_sequence = " ".join(name_sequence)
                result_seq, request_name, len_seq, seq_count_A, seq_count_C, seq_count_G, seq_count_T  = Functions.get_code_gene_sequence_of_dna(str(name_sequence))
                format_parameter = {'a': seq_count_A, 'c':seq_count_C, 'g':seq_count_G, 't': seq_count_T, 'len_seq': len_seq }
                contents = Functions.read_template_html_file('./html/gene_calculations.html', **format_parameter)
            else:
                contents = Functions.read_html_file("./html/error.html")
        # Message to send back to the clinet
        except IndexError:
            contents = Functions.read_html_file("./html/error.html")
        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

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