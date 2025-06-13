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

   

if __name__ == "__main__":
    main()