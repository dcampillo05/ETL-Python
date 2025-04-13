import pandas as pd
import streamlit as st
from validation import sheetVendas
from pydantic import ValidationError

def dataValid(df):
    erros = []
    datasValid = []

    for index, row in df.iterrows():
        try:
            data = row.to_dict()

            userValid = sheetVendas(**data)
            datasValid.append(userValid)

        except ValidationError as e:
            erros.append(f"Erro na linha: {index + 2}: {str:(e)}")

    return datasValid, erros

def main():
    st.title("Validador de dados")
    st.write("Upload do arquivo CSV para validação")

    uploadedFile = st.file_uploader("Escolha um arquivo em CSV")

    if uploadedFile is not None:
        try:
            df = pd.read_csv(uploadedFile)

            st.write("Previews de dados: ")
            st.dataframe(df.head())

            if st.button("Validar dados"):
                with st.spinner("Validando dados..."):
                    datasValid, erros = dataValid(df)

                    if erros:
                        st.error("Foram encontrados erros na validação: ")
                        for erro in erros:
                            st.write(erro)
                    else:
                        st.success("Todos os dados foram validados com sucesso!")

                        st.write(f"TOtal de registros validados: {len(datasValid)}")
                        
                        dfValid = pd.DataFrame([data.dict() for data in datasValid])
                        st.download_button(
                            label = "Download dos dados validados",
                            data = dfValid.to_csv(index = False),
                            file_name = "Dados_Validados.csv",
                            mime = "text/csv"  
                        )
        except Exception as e:
            st.error(f"Erro ao processar o arquivo: {str(e)}")
    
if __name__ == "__main__":
    main()