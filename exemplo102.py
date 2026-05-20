import requests


def buscar_cep(cep):
    # Remove dots and hyphens to ensure only numbers are sent
    cep = cep.replace("-", "").replace(".", "").strip()

    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        if "erro" not in dados:
            return dados
        else:
            return "CEP not found."
    else:
        return "Request error."



resultado = buscar_cep("58910-000")
print(resultado)