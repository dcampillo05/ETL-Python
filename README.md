# 🧪 ETL Validador de Dados com Streamlit

Este projeto é uma aplicação interativa desenvolvida em **Python** com **Streamlit** para realizar a **validação de dados de campanhas de marketing**. A validação é feita com o auxílio da biblioteca `Pydantic`, que garante que os dados sigam o formato e as regras estabelecidas pelo modelo `sheetVendas`.

---

## 🚀 Funcionalidades

- Upload de arquivos `.csv`
- Visualização prévia dos dados
- Validação automática com feedback detalhado (linha e tipo de erro)
- Download dos dados validados (sem erros)

---

## ✅ Estrutura de Validação

Os dados devem seguir o seguinte schema:

```python
class sheetVendas(BaseModel):
    Organizador: int
    Ano_Mes: str
    Dia_da_Semana: str
    Tipo_Dia: str
    Objetivo: str
    Date: str
    AdSet_name: Optional[str]
    Amount_spent: float = Field(0.0, ge=0, le=1200.00)
    Link_clicks: Optional[float]
    Impressions: Optional[float]
    Conversions: Optional[float]
    Segmentação: str
    Tipo_de_Anúncio: str
    Fase: str
```

# Como Rodar?

```
streamlit run src/fileValid.py
```
