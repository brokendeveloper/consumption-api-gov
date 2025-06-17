from data.merge import (
    merge_executor_with_uf, merge_meta_with_uf, merge_finalidade_with_uf,
    merge_documento_with_uf, merge_ordem_pagamento_with_uf, merge_historico_pagamento_with_uf,
    merge_plano_trabalho_with_uf, merge_relatorio_gestao_with_uf
)
from data.conversions import export_to_csv

def exportar_csvs(dfs, pasta_saida, filtro_uf=None):
    # Merges
    df_executores_uf = merge_executor_with_uf(dfs['executores'], dfs['planos'])
    df_metas_uf = merge_meta_with_uf(dfs['metas'], dfs['executores'], dfs['planos'])
    df_finalidades_uf = merge_finalidade_with_uf(dfs['finalidades'], dfs['executores'], dfs['planos'])
    df_documentos_uf = merge_documento_with_uf(dfs['documentos'], dfs['empenhos'], dfs['planos'])
    df_ordens_uf = merge_ordem_pagamento_with_uf(dfs['ordens'], df_documentos_uf, dfs['empenhos'], dfs['planos'])
    df_historicos_uf = merge_historico_pagamento_with_uf(dfs['historicos'], df_ordens_uf, df_documentos_uf, dfs['empenhos'], dfs['planos'])
    df_planos_trabalho_uf = merge_plano_trabalho_with_uf(dfs['planos_trabalho'], dfs['planos'])
    df_relatorios_uf = merge_relatorio_gestao_with_uf(dfs['relatorios'], dfs['planos'])

    sufixo = f"_{filtro_uf}" if filtro_uf else ""

    # Filtros
    if filtro_uf:
        df_planos = dfs['planos'][dfs['planos']['uf_beneficiario_plano_acao'] == filtro_uf]
        df_executores_uf = df_executores_uf[df_executores_uf['uf_beneficiario_plano_acao'] == filtro_uf]
        df_metas_uf = df_metas_uf[df_metas_uf['uf_beneficiario_plano_acao'] == filtro_uf]
        df_finalidades_uf = df_finalidades_uf[df_finalidades_uf['uf_beneficiario_plano_acao'] == filtro_uf]
        df_empenhos = dfs['empenhos'][dfs['empenhos']['uf_beneficiario_empenho'] == filtro_uf]
        df_documentos_uf = df_documentos_uf[df_documentos_uf['uf_beneficiario_plano_acao'] == filtro_uf]
        df_ordens_uf = df_ordens_uf[df_ordens_uf['uf_beneficiario_plano_acao'] == filtro_uf]
        df_historicos_uf = df_historicos_uf[df_historicos_uf['uf_beneficiario_plano_acao'] == filtro_uf]
        df_planos_trabalho_uf = df_planos_trabalho_uf[df_planos_trabalho_uf['uf_beneficiario_plano_acao'] == filtro_uf]
        df_relatorios_uf = df_relatorios_uf[df_relatorios_uf['uf_beneficiario_plano_acao'] == filtro_uf]
    else:
        df_planos = dfs['planos']
        df_empenhos = dfs['empenhos']

    # Exportação
    export_to_csv(df_planos, f'{pasta_saida}/plano_acao_especial{sufixo}.csv')
    export_to_csv(df_executores_uf, f'{pasta_saida}/executor_especial{sufixo}.csv')
    export_to_csv(df_metas_uf, f'{pasta_saida}/meta_especial{sufixo}.csv')
    export_to_csv(df_finalidades_uf, f'{pasta_saida}/finalidade_especial{sufixo}.csv')
    export_to_csv(df_empenhos, f'{pasta_saida}/empenho_especial{sufixo}.csv')
    export_to_csv(df_documentos_uf, f'{pasta_saida}/documento_habil_especial{sufixo}.csv')
    export_to_csv(df_ordens_uf, f'{pasta_saida}/ordem_pagamento_ordem_bancaria_especial{sufixo}.csv')
    export_to_csv(df_historicos_uf, f'{pasta_saida}/historico_pagamento_especial{sufixo}.csv')
    export_to_csv(df_planos_trabalho_uf, f'{pasta_saida}/plano_trabalho_especial{sufixo}.csv')
    export_to_csv(df_relatorios_uf, f'{pasta_saida}/relatorio_gestao_especial{sufixo}.csv')