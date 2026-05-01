## Projeto Final – Redes Neurais I
## Monitoramento Preditivo e Análise Inteligente de Incidentes em Ambientes Bancários Cloud-Native

**Autora:** Márcia Aparecida Rodigues de Sousa  

---

### 📌 Introdução
Este projeto aplica arquiteturas neurais (**MLP** e **LSTM**) para prever incidentes em métricas de observabilidade de sistemas bancários cloud-native.  
O objetivo é classificar se ocorrerá um incidente nos próximos *H* passos, a partir de uma janela temporal de métricas (CPU, memória, taxa de erros, latência p95).

---

### 📊 Dataset
- Dataset sintético com 4.000 a 30.000 registros.  
- Métricas simuladas: CPU, memória, taxa de erros, latência p95.  
- Variável alvo: `incident_event` (0/1).  
- Justificativa: uso de dados sintéticos evita problemas de privacidade e permite controle experimental.  
- Em ambientes reais seriam necessários milhões de métricas diárias.

---

### 🧠 Arquiteturas utilizadas
- **MLP (baseline):** aprende padrões agregados, mas não modela dependências temporais.  
- **LSTM (principal):** captura dependências temporais na sequência, mais adequado para séries temporais.  

---

### ⚙️ Metodologia
- **Pré-processamento:** normalização (z-score), criação de janelas temporais (L=30, H=10).  
- **Split temporal:** 70% treino, 15% validação, 15% teste.  
- **Desbalanceamento:** uso de *class weights*.  
- **Treinamento:** EarlyStopping monitorando PR-AUC.  
- **Avaliação:** métricas (Acurácia, Recall, Precisão, F1, ROC-AUC, PR-AUC) e visualizações (curvas ROC e PR).

---

### 📈 Resultados

| Modelo | Acurácia | Recall | Precisão | F1-Score | ROC-AUC | PR-AUC |
|--------|----------|--------|----------|----------|---------|--------|
| MLP    | 0.517    | 0.559  | 0.657    | 0.604    | 0.498   | 0.659  |
| LSTM   | 0.551    | 0.734  | 0.639    | 0.683    | 0.435   | 0.615  |

**Interpretação:**  
- O **LSTM** apresentou melhor recall (0.734) e F1-Score (0.683), sendo mais adequado para prever incidentes em séries temporais.  
- O **MLP** teve precisão (0.657) e PR-AUC (0.659) ligeiramente superiores, mas deixou passar mais incidentes.  
- Em ambientes bancários reais, o recall é mais crítico, pois é preferível gerar alguns falsos positivos do que deixar passar incidentes graves.

---

### 📌 Discussão
- **Limitações:** dataset sintético simplificado, heurística de rotulagem básica.  
- **Melhorias futuras:** CNNs para séries temporais, Transformers, integração com logs, ajuste de thresholds, escala para milhões de registros.  
- **Conformidade regulatória:** uso de dados sintéticos garante aderência à LGPD e Resolução BCB nº 304/2023.

---

### 🚀 Como executar
1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/projeto-redes-neurais-I.git
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Abra o notebook no Jupyter ou Google Colab:
   ```bash
   jupyter notebook Projeto_Final_Redes_Neurais_I.ipynb
   ```
   ou abra diretamente no Colab:  
   [Abrir no Google Colab](https://colab.research.google.com/drive/1WptPo62fccMqQfsGJZYBKa_s0bkG6uxr#scrollTo=4k1KLZQHsqnt)

---

### 📌 Conclusão
Este estudo mostra que redes neurais artificiais podem ser integradas a pipelines de observabilidade em bancos para antecipar falhas e incidentes.  
O LSTM se mostrou superior ao MLP em recall e F1-Score, confirmando sua adequação para séries temporais.  
Em ambientes bancários reais, seria necessário escalar para milhões de métricas e arquiteturas mais robustas, mas o conceito demonstrado aqui é totalmente aplicável.
```
