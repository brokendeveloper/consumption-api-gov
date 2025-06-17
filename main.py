from api import endpoints
from data.processing import to_dataframe
from data.export import exportar_csvs

def baixar_todos_os_dados():
    return {
        'planos': to_dataframe(endpoints.get_plano_acao_especial()),
        'executores': to_dataframe(endpoints.get_executor_especial()),
        'metas': to_dataframe(endpoints.get_meta_especial()),
        'finalidades': to_dataframe(endpoints.get_finalidade_especial()),
        'empenhos': to_dataframe(endpoints.get_empenho_especial()),
        'documentos': to_dataframe(endpoints.get_documento_habil_especial()),
        'ordens': to_dataframe(endpoints.get_ordem_pagamento_ordem_bancaria_especial()),
        'historicos': to_dataframe(endpoints.get_historico_pagamento_especial()),
        'planos_trabalho': to_dataframe(endpoints.get_plano_trabalho_especial()),
        'relatorios': to_dataframe(endpoints.get_relatorio_gestao_especial()),
    }

def main():
    dfs = baixar_todos_os_dados()
    exportar_csvs(dfs, pasta_saida='csv_without_filter')
    exportar_csvs(dfs, pasta_saida='csv_with_filter/arquivos', filtro_uf='PE')

if __name__ == "__main__":
    main()