# 📊 Previsor IA  – Dashboard Inteligente de Vendas

O **Previsor IA ** é uma aplicação interativa que permite ao usuário analisar dados históricos de vendas, gerar previsões futuras com modelos de Inteligência Artificial (IA) e visualizar tudo em gráficos interativos. Com uma interface amigável em **Streamlit**, o projeto torna a análise e previsão acessível para qualquer área da empresa.

---

## 🚀 Funcionalidades

✅ Upload de arquivo CSV com colunas `data` e `vendas`  
✅ Análise Exploratória de Dados (EDA) com métricas visuais:
- Total de vendas
- Média diária
- Pico de vendas
- Gráfico de linha com tendência histórica  

✅ Escolha dinâmica do número de dias para previsão (7 a 90)  
✅ Geração de previsão com IA (modelo Prophet)  
✅ Gráfico interativo com previsão e intervalo de confiança  
✅ Download do CSV com os resultados da previsão

---

## 📁 Estrutura do Projeto

```
previsor-ia-v2/
├── app.py                # Aplicação principal em Streamlit
├── previsao.py           # Lógica da previsão com Prophet
├── vendas_exemplo.csv    # Arquivo de dados fictício para teste
├── requirements.txt      # Lista de dependências Python

```

---

## 📦 Requisitos

- Python 3.8+
- Bibliotecas: `streamlit`, `pandas`, `plotly`, `prophet`

---

## 🧪 Como usar

### 1. Clone ou baixe o projeto

```bash
git clone https://github.com/jpcoutolm/previsor-ia.git
cd previsor-ia
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Rode o app

```bash
streamlit run app.py
```

Abra no navegador: http://localhost:8501

---

## 📄 Formato esperado do CSV

```csv
data,vendas
2024-01-01,150
2024-01-02,162
2024-01-03,140
...
```

---

## ☁️ Sugestão de deploy (caso deseje publicar)

- [Streamlit Cloud](https://streamlit.io/cloud)
- [Render](https://render.com)
- [Railway](https://railway.app)

---

## 🧠 Tecnologias utilizadas

- **Python** – Linguagem principal
- **Streamlit** – Framework para apps interativos
- **Prophet** – Biblioteca de previsão de séries temporais desenvolvida pelo Facebook
- **Plotly** – Gráficos interativos e responsivos
- **Pandas** – Manipulação de dados

---

## 🤝 Contribuição

Sinta-se livre para:
- Sugerir melhorias
- Reportar bugs
- Criar novas funcionalidades (ex: múltiplos produtos, login, banco de dados)

---

## 👨‍💻 Autor

**João Pedro do Couto**  
Estudante de Engenharia da Computação  
Desenvolvedor e entusiasta de IA aplicada a negócios  
📧 [joaopedrodocouto77@gmail.com] 

---

## 📜 Licença

Este projeto está sob a licença MIT – veja o arquivo [LICENSE](LICENSE) para detalhes.
