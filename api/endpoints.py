from .client import APIClient

client = APIClient()

def get_programa_especial(params=None):
    return client.get("/programa_especial", params)

def get_plano_acao_especial(params=None):
    return client.get("/plano_acao_especial", params)

def get_empenho_especial(params=None):
    return client.get("/empenho_especial", params)

def get_documento_habil_especial(params=None):
    return client.get("/documento_habil_especial", params)

def get_ordem_pagamento_ordem_bancaria_especial(params=None):
    return client.get("/ordem_pagamento_ordem_bancaria_especial", params)

def get_historico_pagamento_especial(params=None):
    return client.get("/historico_pagamento_especial", params)

def get_relatorio_gestao_especial(params=None):
    return client.get("/relatorio_gestao_especial", params)

def get_meta_especial(params=None):
    return client.get("/meta_especial", params)

def get_executor_especial(params=None):
    return client.get("/executor_especial", params)

def get_plano_trabalho_especial(params=None):
    return client.get("/plano_trabalho_especial", params)

def get_finalidade_especial(params=None):
    return client.get("/finalidade_especial", params)