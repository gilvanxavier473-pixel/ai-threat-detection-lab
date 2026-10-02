# 🔐 AI Threat Detection Lab 2.1

Laboratório educacional de Cibersegurança desenvolvido em Python, com foco em **Blue Team, SOC e detecção de ameaças em aplicações de Inteligência Artificial**.

**Autor:** Gilvan Xavier  
**Status:** Projeto educacional ativo

## 🎯 Objetivo

Transformar conhecimentos de Segurança da Informação em prática por meio de um laboratório local e controlado. O projeto simula detecção, classificação, bloqueio e registro de eventos suspeitos.

## 🛡️ Funcionalidades

- Detecção de Prompt Injection
- Classificação de ameaças por severidade
- Bloqueio simulado de ações suspeitas
- Logging de eventos
- Dashboard SOC com Streamlit
- Testes automatizados com Pytest

## 🏗️ Estrutura

```text
ai-threat-detection-lab-2.1/
├── app.py
├── detector.py
├── logger.py
├── sandbox.py
├── requirements.txt
├── README.md
├── .gitignore
├── config/
├── dashboard/
├── logs/
├── reports/
└── tests/
```

## ⚙️ Como executar no Windows

```bash
py -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python app.py
```

Para abrir o dashboard:

```bash
streamlit run dashboard/app.py
```

Depois acesse `http://localhost:8501`.

Para executar os testes:

```bash
pytest
```

## 🧰 Tecnologias

Python • Streamlit • Pandas • Pytest • Git • GitHub

## 📚 Conceitos estudados

Blue Team • SOC • Threat Detection • Prompt Injection • Logging • Security Monitoring • Sandbox Isolation • Security Guardrails

## ⚠️ Aviso

Projeto educacional para uso em ambiente controlado. As funcionalidades de bloqueio e execução são simulações destinadas ao aprendizado de conceitos de defesa.

## 👨‍💻 Autor

**Gilvan Xavier** — Estudante de Segurança da Informação, com interesse em Cibersegurança, Blue Team, SOC e Infraestrutura de TI.
