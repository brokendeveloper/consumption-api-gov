from api import endpoints
from data import processing

def main():
    
    print("Baixando dados de programa_especial...")
    programas = endpoints.get_programa_especial()
    df_programas = processing.to_dataframe(programas)
    processing.show_dataframe(df_programas)

    print("Baixando dados de plano_acao_especial...")
    planos = endpoints.get_plano_acao_especial()
    df_planos = processing.to_dataframe(planos)
    processing.show_dataframe(df_planos)

    print("Baixando dados de empenho_especial...")
    empenhos = endpoints.get_empenho_especial()
    df_empenhos = processing.to_dataframe(empenhos)
    processing.show_dataframe(df_empenhos)

    print("Baixando dados de documento_habil_especial...")
    documentos = endpoints.get_documento_habil_especial()
    df_documentos = processing.to_dataframe(documentos)
    processing.show_dataframe(df_documentos)

    print("Baixando dados de ordem_pagamento_ordem_bancaria_especial...")
    ordens_pagamento = endpoints.get_ordem_pagamento_ordem_bancaria_especial()
    df_ordens_pagamento = processing.to_dataframe(ordens_pagamento)
    processing.show_dataframe(df_ordens_pagamento)

    print("Baixando dados de historico_pagamento_especial...")
    historicos_pagamento = endpoints.get_historico_pagamento_especial()
    df_historicos_pagamento = processing.to_dataframe(historicos_pagamento)
    processing.show_dataframe(df_historicos_pagamento)

    print("Baixando dados de relatorio_gestao_especial...")
    relatorios_gestao = endpoints.get_relatorio_gestao_especial()
    df_relatórios_gestao = processing.to_dataframe(relatorios_gestao)
    processing.show_dataframe(df_relatórios_gestao)

    print("Baixando dados de meta_especial...")
    metas = endpoints.get_meta_especial()
    df_metas = processing.to_dataframe(metas)
    processing.show_dataframe(df_metas)

    print("Baixando dados de executor_especial...")
    executores = endpoints.get_executor_especial()
    df_executores = processing.to_dataframe(executores)
    processing.show_dataframe(df_executores)

    print("Baixando dados de plano_trabalho_especial...")
    planos_trabalho = endpoints.get_plano_trabalho_especial()
    df_planos_trabalho = processing.to_dataframe(planos_trabalho)
    processing.show_dataframe(df_planos_trabalho)

    print("Baixando dados de finalidade_especial...")
    finalidades = endpoints.get_finalidade_especial()
    df_finalidades = processing.to_dataframe(finalidades)
    processing.show_dataframe(df_finalidades)

    print("Todos os dados foram baixados e processados com sucesso!")
    
   

if __name__ == "__main__":
    main()