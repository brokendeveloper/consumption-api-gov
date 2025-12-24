from .client import APIClient

client = APIClient()

def get_plano_acao_especial(params=None):
    return client.get("/plano_acao_especial", params)

def get_plano_trabalho_especial(params=None):
    return client.get("/plano_trabalho_especial", params)