import Seq1 as s1
import http.client
import json

genes_dict = {'FRAT1': 'ENSG00000165879 ', 'ADA': 'ENSG00000196839',
              'FXN': 'ENSG00000165060', "RNU6_269P": 'ENSG00000212379',
              'MIR633': 'ENSG00000207552', 'TTTY4C': 'ENSG00000228296',
              'RBMY2YP': 'ENSG00000227633', 'FGFR3': 'ENSG00000068078',
              'KDR': 'ENSG00000128052', 'ANK2': 'ENSG00000248152'}
SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id"
PARAMETERS = '?content-type=application/json'

connection = http.client.HTTPConnection(SERVER)
try:
    for id in genes_dict.values():
        connection.request("Get", ENDPOINT + id + PARAMETERS)
        response = connection.getresponse()
        if response.status == 200:
            response_dict = json.loads(response.read().decode())
            sequences = s1.Seq(response_dict["seq"])
            s_length = sequences.len()
            percentage = sequences.percentage_base(sequences.count_bases(), s_length)
            most_frequent_base = sequences.frequent_base(sequences.count())
            print(('total len: ', most_frequent_base))
except KeyError:

    print("the gene is not in the list.Choose one of the following", list(genes_dict.keys()))
