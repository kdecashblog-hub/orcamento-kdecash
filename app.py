import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="KDE Cash | Orçamento Doméstico",
    layout="centered"
)

st.title("💰 Orçamento Doméstico – KDE Cash")
st.write("Controle seus gastos e visualize seu saldo de forma simples e educativa.")

# Inicialização dos dados
if "dados" not in st.session_state:
    st.session_state.dados = pd.DataFrame(
        columns=["Descrição", "Categoria", "Valor"]
    )

# Entrada da renda
renda = st.number_input(
    "Informe sua renda mensal (R$)",
    min_value=0.0,
    step=100.0
)

st.divider()

# Formulário de gastos
with st.form("form_gasto"):
    descricao = st.text_input("Descrição do gasto")
    categoria = st.selectbox(
        "Categoria",
        ["Moradia", "Alimentação", "Transporte", "Lazer", "Outros"]
    )
    valor = st.number_input("Valor do gasto (R$)", min_value=0.0)
    adicionar = st.form_submit_button("Adicionar gasto")

    if adicionar and descricao and valor > 0:
        novo = pd.DataFrame(
            [[descricao, categoria, valor]],
            columns=["Descrição", "Categoria", "Valor"]
        )
        st.session_state.dados = pd.concat(
            [st.session_state.dados, novo],
            ignore_index=True
        )

# Dashboard
st.divider()

total_gastos = st.session_state.dados["Valor"].sum()
saldo = renda - total_gastos

col1, col2, col3 = st.columns(3)
col1.metric("Renda", f"R$ {renda:,.2f}")
col2.metric("Gastos", f"R$ {total_gastos:,.2f}")
col3.metric("Saldo", f"R$ {saldo:,.2f}")

# Tabela
st.subheader("📋 Lista de Gastos")
st.dataframe(st.session_state.dados, use_container_width=True)

# Gráfico
if not st.session_state.dados.empty:
    st.subheader("📊 Gastos por Categoria")
    grafico = (
        st.session_state.dados
        .groupby("Categoria")["Valor"]
        .sum()
    )
    st.bar_chart(grafico)

# Reset
if st.button("Limpar orçamento"):
    st.session_state.dados = pd.DataFrame(
        columns=["Descrição", "Categoria", "Valor"]
    )

st.divider()

st.caption(
    "Ferramenta educativa. Não constitui recomendação financeira."
)
