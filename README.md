# Controle de Frequência e Absenteísmo

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

## English

### Problem
HR teams often track attendance in scattered spreadsheets, which makes it hard to see how much absenteeism weighs and where it concentrates. This project simulates that scenario and answers: **what is the overall absenteeism rate, and in which months and departments does it concentrate?**

### How I built the solution
1. Generated a synthetic dataset with a fixed seed (reproducible, no real personal data).
2. Validated the data: no null values and unique employee IDs.
3. Calculated the overall absenteeism rate (absences + medical certificates) with Pandas.
4. Grouped the data by month, department and employee to find patterns.
5. Built 4 charts with Matplotlib and wrote bilingual conclusions in the notebook.

### Technologies
Python, Pandas, NumPy, Matplotlib, Kaggle Notebooks, Git/GitHub.

### Results
- Dataset: 50 employees and 13,050 attendance records.
- Overall absenteeism rate: **7.10%**.
- Highest month: **May (8.82%)**. Lowest: **March (6.10%)**.
- Highest department: **Atendimento (10.92%)**. Lowest: **Financeiro (6.19%)**.
- Employee with the most delay minutes: **F030 (837 min)**.
- Takeaway: Atendimento's rate is about 4.7 percentage points above Financeiro's, so it is the first area to investigate.

### Learnings
- How to generate reproducible synthetic data (fixed seed).
- How to validate data quality before analyzing it.
- How to turn raw records into business indicators and compare groups.
- Good practices with Git, project structure and data privacy (LGPD).

### How to run
1. Open the notebook on Kaggle: **[https://www.kaggle.com/code/klaytonsilva/controle-de-frequ-ncia-e-absente-smo]**.
2. Click "Run All". The first cell installs the dependencies and the data is generated automatically, with no local files needed.

To run elsewhere: install the packages from `requirements.txt` and run the notebook in `notebooks/`.

> All data is 100% synthetic. No real personal information is used.

---

## Português

### Problema
Times de RH costumam controlar a frequência em planilhas espalhadas, o que dificulta enxergar quanto o absenteísmo pesa e onde ele se concentra. Este projeto simula esse cenário e responde: **qual é a taxa geral de absenteísmo e em quais meses e departamentos ela se concentra?**

### Como desenvolvi a solução
1. Gerei uma base sintética com seed fixa (reproduzível, sem dados pessoais reais).
2. Validei os dados: sem valores nulos e com IDs de funcionários únicos.
3. Calculei a taxa geral de absenteísmo (faltas + atestados) com Pandas.
4. Agrupei os dados por mês, departamento e funcionário para encontrar padrões.
5. Criei 4 gráficos com Matplotlib e escrevi conclusões bilíngues no notebook.

### Tecnologias utilizadas
Python, Pandas, NumPy, Matplotlib, Kaggle Notebooks, Git/GitHub.

### Resultados alcançados
- Base com 50 funcionários e 13.050 registros de frequência.
- Taxa geral de absenteísmo: **7,10%**.
- Mês mais alto: **maio (8,82%)**. Mais baixo: **março (6,10%)**.
- Departamento mais alto: **Atendimento (10,92%)**. Mais baixo: **Financeiro (6,19%)**.
- Funcionário com mais minutos de atraso: **F030 (837 min)**.
- Conclusão: a taxa de Atendimento está cerca de 4,7 pontos percentuais acima da de Financeiro, então é a primeira área a investigar.

### Aprendizados obtidos
- Como gerar dados sintéticos reproduzíveis (seed fixa).
- Como validar a qualidade dos dados antes de analisar.
- Como transformar registros brutos em indicadores de negócio e comparar grupos.
- Boas práticas de Git, organização de projeto e privacidade de dados (LGPD).

### Como executar
1. Abra o notebook no Kaggle: **[https://www.kaggle.com/code/klaytonsilva/controle-de-frequ-ncia-e-absente-smo]**.
2. Clique em "Run All". A primeira célula instala as dependências e os dados são gerados automaticamente, sem precisar de arquivos locais.

Para rodar em outro lugar: instale os pacotes do `requirements.txt` e execute o notebook da pasta `notebooks/`.

> Todos os dados são 100% sintéticos. Nenhuma informação pessoal real é usada.

---

## Estrutura de pastas / Folder structure

```
.
├── data/          # dados / data
├── notebooks/     # notebook principal / main notebook
├── src/           # código / code
├── reports/       # relatórios / reports
├── .env.example   # modelo de variáveis, sem valores reais / template, no real values
├── .gitignore
├── requirements.txt
└── README.md
```
