import pandas as pd

def merge_executor_with_uf(df_executores, df_planos):
    """Adiciona UF ao executor via id_plano_acao."""
    merged = df_executores.merge(
        df_planos[['id_plano_acao', 'uf_beneficiario_plano_acao']],
        on='id_plano_acao', how='left'
    )
    return merged

def merge_meta_with_uf(df_metas, df_executores, df_planos):
    """Adiciona UF à meta via executor e plano de ação."""
    merged = df_metas.merge(
        df_executores[['id_executor', 'id_plano_acao']],
        on='id_executor', how='left'
    ).merge(
        df_planos[['id_plano_acao', 'uf_beneficiario_plano_acao']],
        on='id_plano_acao', how='left'
    )
    return merged

def merge_finalidade_with_uf(df_finalidades, df_executores, df_planos):
    """Adiciona UF à finalidade via executor e plano de ação."""
    merged = df_finalidades.merge(
        df_executores[['id_executor', 'id_plano_acao']],
        on='id_executor', how='left'
    ).merge(
        df_planos[['id_plano_acao', 'uf_beneficiario_plano_acao']],
        on='id_plano_acao', how='left'
    )
    return merged

def merge_documento_with_uf(df_documentos, df_empenhos, df_planos):
    """Adiciona UF ao documento hábil via empenho e plano de ação."""
    merged = df_documentos.merge(
        df_empenhos[['id_empenho', 'id_plano_acao']],
        on='id_empenho', how='left'
    ).merge(
        df_planos[['id_plano_acao', 'uf_beneficiario_plano_acao']],
        on='id_plano_acao', how='left'
    )
    return merged

def merge_ordem_pagamento_with_uf(df_ordens, df_documentos, df_empenhos, df_planos):
    """Adiciona UF à ordem de pagamento via documento, empenho e plano de ação."""
    merged = df_ordens.merge(
        df_documentos[['id_dh', 'id_empenho']],
        on='id_dh', how='left'
    ).merge(
        df_empenhos[['id_empenho', 'id_plano_acao']],
        on='id_empenho', how='left'
    ).merge(
        df_planos[['id_plano_acao', 'uf_beneficiario_plano_acao']],
        on='id_plano_acao', how='left'
    )
    return merged

def merge_historico_pagamento_with_uf(df_historicos, df_ordens, df_documentos, df_empenhos, df_planos):
    """Adiciona UF ao histórico de pagamento via ordem, documento, empenho e plano de ação."""
    merged = df_historicos.merge(
        df_ordens[['id_op_ob', 'id_dh']],
        on='id_op_ob', how='left'
    ).merge(
        df_documentos[['id_dh', 'id_empenho']],
        on='id_dh', how='left'
    ).merge(
        df_empenhos[['id_empenho', 'id_plano_acao']],
        on='id_empenho', how='left'
    ).merge(
        df_planos[['id_plano_acao', 'uf_beneficiario_plano_acao']],
        on='id_plano_acao', how='left'
    )
    return merged

def merge_plano_trabalho_with_uf(df_planos_trabalho, df_planos):
    """Adiciona UF ao plano de trabalho via plano de ação."""
    merged = df_planos_trabalho.merge(
        df_planos[['id_plano_acao', 'uf_beneficiario_plano_acao']],
        on='id_plano_acao', how='left'
    )
    return merged

def merge_relatorio_gestao_with_uf(df_relatorios, df_planos):
    """Adiciona UF ao relatório de gestão via plano de ação."""
    merged = df_relatorios.merge(
        df_planos[['id_plano_acao', 'uf_beneficiario_plano_acao']],
        on='id_plano_acao', how='left'
    )
    return merged