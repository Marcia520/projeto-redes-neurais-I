import streamlit as st
import numpy as np
import pickle

# Carregar modelos e scaler
mlp = pickle.load(open("mlp_model.pkl", "rb"))
lstm = pickle.load(open("lstm_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("Previsão de Incidentes Bancários - AIOps")

st.markdown("""
Aplicação baseada em Redes Neurais para prever se haverá **incidente** 
nos próximos passos, com base em métricas de observabilidade.
""")

# Escolha do modelo
modelo_escolhido = st.radio(
    "Selecione o modelo para previsão:",
    ("MLP", "LSTM")
)

# Entradas do usuário
cpu = st.slider("Uso de CPU (%)", 0, 100, 50)
memoria = st.slider("Uso de Memória (%)", 0, 100, 60)
erros = st.number_input("Taxa de Erros", min_value=0, value=1)
latencia = st.number_input("Latência p95 (ms)", min_value=0, value=180)

# Pré-processamento
X_input = np.array([[cpu, memoria, erros, latencia]])
X_input_scaled = scaler.transform(X_input)

# Previsão
if modelo_escolhido == "MLP":
    proba = mlp.predict_proba(X_input_scaled)[0][1]
    pred = (proba >= 0.5).astype(int)
else:
    # Para LSTM, reshape para sequência (1 janela, 30 passos, 4 features)
    # Aqui simplificamos para 1 passo, mas você pode adaptar
    X_seq = np.expand_dims(X_input_scaled, axis=1)  
    proba = lstm.predict(X_seq)[0][0]
    pred = (proba >= 0.5).astype(int)

# Saída
st.subheader("Resultado da Previsão")
st.write("Modelo usado:", modelo_escolhido)
st.write("Probabilidade de incidente:", round(float(proba), 3))
st.write("Classificação:", "🚨 Incidente" if pred == 1 else "✅ Normal")
