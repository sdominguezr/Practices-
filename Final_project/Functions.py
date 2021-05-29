import pathlib
import jinja2
import requests


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

def get_karyotype(name_specie):
    endpoint = "https://rest.ensembl.org/info/assembly/" + name_specie
    request = requests.get(endpoint, headers={"Content-Type": "application/json"})
    if not request.ok:
        request.raise_for_status()
    else:
        result_karyotype = request.json()['karyotype']
    return result_karyotype
def get_length_chromosome(specie, number_chromosome):
    endpoint = "https://rest.ensembl.org/info/assembly/" + specie
    request = requests.get(endpoint, headers={"Content-Type" : "application/json"})
    if not request.ok:
        request.raise_for_status()
    else:
        result_chromosome = request.json()['top_level_region'][number_chromosome - 1]['length']
        #result_chromosome [str(number_chromosome-1)]['length']
    return  result_chromosome



