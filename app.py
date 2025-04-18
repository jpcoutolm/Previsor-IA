import streamlit as st
import pandas as pd
from previsao import gerar_previsao
import io

st.set_page_config(page_title="Previsor IA", layout="wide")
st.title("📊 Previsor IA  – Dashboard Inteligente de Vendas")

uploaded_file = st.file_uploader("📁 Faça upload do arquivo CSV com colunas: data, vendas", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file, parse_dates=["data"])
    
    # EDA básica
    st.subheader("🔍 Análise Exploratória (EDA)")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total de Vendas", f"{df['vendas'].sum():,.0f}")
    col2.metric("Média Diária", f"{df['vendas'].mean():.2f}")
    max_day = df.loc[df['vendas'].idxmax()]
    col3.metric("Pico de Vendas", f"{max_day['vendas']} em {max_day['data'].date()}")

    # Gráfico de linha simples
    st.line_chart(df.set_index("data")["vendas"])

    # Slider de previsão
    st.subheader("📅 Escolha o número de dias para previsão")
    dias = st.slider("Dias para prever", min_value=7, max_value=90, value=30, step=1)

    # Geração da previsão
    st.subheader("📈 Resultado da Previsão")
    fig, forecast_result = gerar_previsao(df, dias)
    st.plotly_chart(fig, use_container_width=True)

    # Botão de download da previsão
    csv_buffer = io.StringIO()
    forecast_result.to_csv(csv_buffer, index=False)
    st.download_button("📥 Baixar CSV com Previsão", data=csv_buffer.getvalue(),
                       file_name="previsao.csv", mime="text/csv")
