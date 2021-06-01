import pathlib
import jinja2
import requests
from urllib.parse import parse_qs

def read_html_file(filename):
    content = pathlib.Path(filename).read_text()
    return content


def read_template_html_file(filename, **kwargs):
    content = jinja2.Template(pathlib.Path(filename).read_text()).render(kwargs)
    return content


# Return len of total species and common names of sublist species
def get_info_species(limit):
    endpoint = "http://rest.ensembl.org/info/species"
    request = requests.get(endpoint, headers={"Content-Type": "application/json"})

    if not request.ok:
        request.raise_for_status()
    else:
        species = request.json()['species']
        common_names = []
        for specie in species[0:limit]:
            common_names.append(specie['common_name'])

        return len(species), common_names
#return the karyotype of the specie selected
def get_karyotype(name_specie):
    endpoint = "https://rest.ensembl.org/info/assembly/" + name_specie
    request = requests.get(endpoint, headers={"Content-Type": "application/json"})
    if not request.ok:
        request.raise_for_status()
    else:
        result_karyotype = request.json()['karyotype']
    return result_karyotype
#it gets the length of
def get_length_chromosome(specie, number_chromosome):
    endpoint = "https://rest.ensembl.org/info/assembly/" + specie
    request = requests.get(endpoint, headers={"Content-Type" : "application/json"})
    if not request.ok:
        request.raise_for_status()
    else:
        result_chromosome = request.json()['top_level_region'][number_chromosome - 1]['length']
    return  result_chromosome

def get_code_gene_sequence_of_dna(name_sequence):
    endpoint = "https://rest.ensembl.org/xrefs/symbol/" + 'homo_sapiens/'+ name_sequence
    request = requests.get(endpoint, headers={"Content-Type" : "application/json"})
    if not request.ok:
        request.raise_for_status()
    else:
        request_name = request.json()[0]['id']
        endpoint_2 ="https://rest.ensembl.org/sequence/id/" + request_name
        request_2 = requests.get(endpoint_2, headers={ "Content-Type" : "application/json"})
        result_seq =request_2.json()['seq']
        len_seq =  str(len(result_seq))
        sequence_list = list(result_seq)
        seq_count_A = round((sequence_list.count('A') / len(result_seq) * 100 ), 2)
        seq_count_C = round((sequence_list.count('C') / len(result_seq) * 100 ), 2)
        seq_count_G = round((sequence_list.count('G') / len(result_seq) * 100 ), 2)
        seq_count_T = round((sequence_list.count('T') / len(result_seq) * 100 ), 2)
    return result_seq, request_name, len_seq, seq_count_A, seq_count_C, seq_count_G, seq_count_T

def get_start_end(name_sequence):
    endpoint = "https://rest.ensembl.org/xrefs/symbol/" + 'homo_sapiens/'+ name_sequence
    request = requests.get(endpoint, headers={"Content-Type" : "application/json"})
    if not request.ok:
        request.raise_for_status()
    else:
        request_name = request.json()[0]['id']
        endpoint_2 = "https://rest.ensembl.org/overlap/id/" + request_name + "?feature=gene"
        request_2 = requests.get(endpoint_2, headers={ "Content-Type" : "application/json"})
        result_start = request_2.json()[0]['start']
        result_end = request_2.json()[0]['end']
    return result_start,result_end





