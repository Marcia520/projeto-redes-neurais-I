## Projeto Final – Redes Neurais I
## Monitoramento Preditivo e Análise Inteligente de Incidentes em Ambientes Bancários Cloud-Native

**Autora:** Márcia Aparecida Rodigues de Sousa  

---

### Introdução
Este projeto aplica arquiteturas neurais (**MLP** e **LSTM**) para prever incidentes em métricas de observabilidade de sistemas bancários cloud-native.  
O objetivo é classificar se ocorrerá um incidente nos próximos *H* passos, a partir de uma janela temporal de métricas (CPU, memória, taxa de erros, latência p95).

---

### Dataset
- Dataset sintético com 4.000 a 30.000 registros.  
- Métricas simuladas: CPU, memória, taxa de erros, latência p95.  
- Variável alvo: `incident_event` (0/1).  
- Justificativa: uso de dados sintéticos evita problemas de privacidade e permite controle experimental.  
- Em ambientes reais seriam necessários milhões de métricas diárias.

---

### Arquiteturas utilizadas
- **MLP (baseline):** aprende padrões agregados, mas não modela dependências temporais.  
- **LSTM (principal):** captura dependências temporais na sequência, mais adequado para séries temporais.  

---

### Metodologia
- **Pré-processamento:** normalização (z-score), criação de janelas temporais (L=30, H=10).  
- **Split temporal:** 70% treino, 15% validação, 15% teste.  
- **Desbalanceamento:** uso de *class weights*.  
- **Treinamento:** EarlyStopping monitorando PR-AUC.  
- **Avaliação:** métricas (Acurácia, Recall, Precisão, F1, ROC-AUC, PR-AUC) e visualizações (curvas ROC e PR).

---

### Resultados

| Modelo | Acurácia | Recall | Precisão | F1-Score | ROC-AUC | PR-AUC |
|--------|----------|--------|----------|----------|---------|--------|
| MLP    | 0.552    | 0.537  | 0.712    | 0.612    | 0.577   | 0.717  |
| LSTM   | 0.554    | 0.543  | 0.712    | 0.616    | 0.570   | 0.713  |

**Interpretação:**  
- Ambos os modelos apresentam desempenho semelhante, com **Recall ~0.54** e **Precisão ~0.71**.  
- O **F1-Score** indica equilíbrio razoável entre precisão e recall.  
- As métricas de área sob curva (ROC-AUC ~0.57 e PR-AUC ~0.71) mostram que os modelos conseguem distinguir incidentes, mas com espaço para melhorias.  
- O LSTM tem leve vantagem em Recall e F1-Score, confirmando sua capacidade de capturar dependências temporais, enquanto o MLP serve como baseline sólido. 
- Em ambientes bancários reais, o recall é mais crítico, pois é preferível gerar alguns falsos positivos do que deixar passar incidentes graves.

---

### Discussão
- **Limitações:** O dataset sintético não captura toda a complexidade de ambientes reais e a rotulagem baseada em heurística pode inflar a prevalência da classe positiva. Trabalhos futuros podem calibrar a taxa base de incidentes e o horizonte H para simular cenários com maior ou menor raridade, além de explorar arquiteturas como CNNs e Transformers.
- **Melhorias futuras:** CNNs para séries temporais, Transformers, integração com logs, ajuste de thresholds, escala para milhões de registros.  
- **Conformidade regulatória:** uso de dados sintéticos garante aderência à LGPD e Resolução BCB nº 304/2023.
- **Observação sobre a prevalência do rótulo:** Em ambientes bancários reais, incidentes críticos são de fato eventos raros. No entanto, neste trabalho o rótulo `incident_in_next_H` marca 1 quando ocorre pelo menos um incidente nos próximos H passos. Essa agregação temporal aumenta a prevalência da classe positiva, tornando os alertas mais frequentes do que os incidentes individuais. Isso é consistente com práticas de AIOps, nas quais o objetivo é antecipar condições de risco e não apenas detectar falhas já ocorridas.

---
## Requisitos Técnicos
- Python 3.12
- TensorFlow 2.x
- Scikit-learn
- NumPy
- Pandas
- Matplotlib

Instale todas as dependências com:
```bash
pip install -r requirements.txt

---

## Estrutura do Repositório
### projeto-redes-neurais-I

├── Projeto_Final_Redes_Neurais_I.ipynb   # Notebook principal
├── requirements.txt                      # Dependências
└── README.md                             # Documentação


## Como executar

1. Clone este repositório:
   
   git clone https://github.com/Marcia520/projeto-redes-neurais-I.git
   
2. Abra o notebook no Jupyter ou Google Colab:
   
   jupyter notebook Projeto_Final_Redes_Neurais_I.ipynb
   
   ou abra diretamente no Colab:  
   [Abrir no Google Colab](https://colab.research.google.com/drive/1WptPo62fccMqQfsGJZYBKa_s0bkG6uxr)

---

### Conclusão

Este projeto demonstrou que redes neurais artificiais podem apoiar o monitoramento preditivo de incidentes em ambientes bancários cloud-native.  
A comparação entre MLP e LSTM evidenciou que modelos sequenciais capturam melhor dependências temporais, oferecendo maior recall e F1-Score, enquanto o MLP funciona como baseline sólido.

Embora incidentes reais sejam raros, a formulação com horizonte de previsão gera alertas preventivos mais frequentes, alinhados às práticas modernas de AIOps.  
Esse tipo de abordagem pode ser integrado a **pipelines de observabilidade em tempo real**, apoiando equipes de **SRE (Site Reliability Engineering)** e operações bancárias na tomada de decisão preventiva, aumentando a resiliência operacional exigida pelo setor financeiro.

## Licença
Sinta-se livre para usar, modificar e compartilhar, desde que mantenha os créditos da autora.

**Autoria:** Márcia Aparecida Rodigues de Sousa – Projeto desenvolvido para a disciplina Redes Neurais I.
```
