from .client import APIClient

client = APIClient()

def get_programa_especial(params=None):
    return client.get("/programa_especial", params)

def get_plano_acao_especial(params=None):
    return client.get("/plano_acao_especial", params)

def get_empenho_especial(params=None):
    return client.get("/empenho_especial", params)