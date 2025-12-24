from api import endpoints
from data.processing import to_dataframe
from data.conversions import export_to_csv, export_to_excel
import os

def baixar_planos_filtrados(cnpj=None, ano_min=None):
    params = {}
    if cnpj:
        params["cnpj_beneficiario_plano_acao"] = f"eq.{cnpj}"
    if ano_min:
        params["ano_plano_acao"] = f"gte.{ano_min}"
    planos = endpoints.get_plano_acao_especial(params)
    return to_dataframe(planos)

def baixar_planos_trabalho_por_ids(ids):
    if not ids:
        return to_dataframe([])
    ids_str = ",".join(str(i) for i in ids)
    params = {"id_plano_acao": f"in.({ids_str})"}
    planos_trabalho = endpoints.get_plano_trabalho_especial(params)
    return to_dataframe(planos_trabalho)

def exportar_dfs(dfs, pasta_saida, sufixo=""):
    os.makedirs(pasta_saida, exist_ok=True)
    for nome, df in dfs.items():
        export_to_csv(df, f"{pasta_saida}/{nome}{sufixo}.csv")
        export_to_excel(df, f"{pasta_saida}/{nome}{sufixo}.xlsx")

def main(cnpj=None, ano_min=None, pasta_saida="output"):
    df_planos = baixar_planos_filtrados(cnpj=cnpj, ano_min=ano_min)
    ids_planos = df_planos['id_plano_acao'].unique().tolist()
    df_planos_trabalho = baixar_planos_trabalho_por_ids(ids_planos)
    dfs = {
        "planos_acao_especial": df_planos,
        "planos_trabalho_especial": df_planos_trabalho
    }
    sufixo = ""
    if cnpj:
        sufixo += f"_CNPJ_{cnpj}"
    if ano_min:
        sufixo += f"_desde_{ano_min}"
    exportar_dfs(dfs, pasta_saida, sufixo)

if __name__ == "__main__":
    # Exemplo: Pernambuco, desde 2020
    main(cnpj="10571982000125", ano_min=2020, pasta_saida="excel_with_filter/2020")