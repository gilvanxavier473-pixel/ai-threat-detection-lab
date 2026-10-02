\# 🔐 AI Threat Detection Lab 2.1



!\[Python](https://img.shields.io/badge/Python-3.14+-blue)

!\[Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)

!\[Security](https://img.shields.io/badge/Security-Blue%20Team-red)

!\[Status](https://img.shields.io/badge/Status-Active-success)



Laboratório educacional de \*\*Cibersegurança desenvolvido em Python\*\*, com foco em \*\*Blue Team, SOC e detecção de ameaças em aplicações de Inteligência Artificial\*\*.



\*\*Autor:\*\* Gilvan Xavier

\*\*Status:\*\* Projeto educacional ativo



\---



\## 🎯 Objetivo



Transformar conhecimentos de Segurança da Informação em prática por meio de um laboratório local e controlado.



O projeto simula a \*\*detecção, classificação, bloqueio e registro de eventos suspeitos\*\*, permitindo estudar conceitos básicos de defesa cibernética.



\---



\## 🛡️ Funcionalidades



\* 🔍 Detecção de Prompt Injection

\* 🚨 Classificação de ameaças por severidade

\* 🔒 Bloqueio simulado de ações suspeitas

\* 📝 Logging de eventos

\* 📊 Dashboard SOC com Streamlit

\* 🧪 Testes automatizados com Pytest



\---



\## 📸 Dashboard SOC



O projeto possui um dashboard desenvolvido com \*\*Streamlit\*\* para visualização dos eventos de segurança.



!\[AI Threat Detection Lab 2.1 Dashboard](dashboard-images/dashboard.png)



O dashboard apresenta informações como:



\* Total de eventos

\* Ameaças detectadas

\* Ações bloqueadas

\* Eventos de alta severidade

\* Ameaças por tipo

\* Eventos por severidade

\* Registro dos eventos de segurança



\---



\## 🏗️ Estrutura



```text

ai-threat-detection-lab-2.1/

│

├── app.py

├── detector.py

├── logger.py

├── sandbox.py

├── requirements.txt

├── README.md

├── .gitignore

├── dashboard-images/

│   └── dashboard.png

├── config/

├── dashboard/

├── logs/

├── reports/

└── tests/

```



\---



\## ⚙️ Como executar no Windows



\### 1. Criar ambiente virtual



```bash

py -m venv .venv

```



\### 2. Ativar o ambiente



```bash

.venv\\Scripts\\activate

```



\### 3. Instalar as dependências



```bash

python -m pip install -r requirements.txt

```



\### 4. Executar o laboratório



```bash

python app.py

```



\### 5. Executar o Dashboard



```bash

streamlit run dashboard/app.py

```



Depois acesse:



```text

http://localhost:8501

```



\---



\## 🧪 Testes



Para executar os testes automatizados:



```bash

pytest

```



\---



\## 🧰 Tecnologias



\* Python

\* Streamlit

\* Pandas

\* Pytest

\* Git

\* GitHub



\---



\## 📚 Conceitos estudados



\* 🔐 Blue Team

\* 🛡️ SOC

\* 🚨 Threat Detection

\* 🤖 Prompt Injection

\* 📝 Logging

\* 📊 Security Monitoring

\* 🔒 Sandbox Isolation

\* 🧱 Security Guardrails



\---



\## 🎓 Objetivo educacional



Este projeto faz parte da minha jornada de aprendizado em \*\*Segurança da Informação\*\*, buscando transformar os conhecimentos adquiridos durante minha formação em experiências práticas.



O laboratório foi desenvolvido para execução em ambiente local e controlado, exclusivamente para fins educacionais.



\---



\## 👨‍💻 Autor



\*\*Gilvan Xavier\*\*



Estudante de Segurança da Informação com interesse em:



\* Cibersegurança

\* Blue Team

\* SOC

\* Infraestrutura de TI

\* Redes

\* Python



\---



\## ⭐ Projeto



Se este projeto foi útil para seus estudos, considere deixar uma ⭐ no repositório.



\*\*GitHub:\*\*

https://github.com/gilvanxavier473-pixel/ai-threat-detection-lab



