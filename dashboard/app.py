import sys
from pathlib import Path

import streamlit as st
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from logger import read_events

st.set_page_config(
    page_title="AI Threat Detection SOC",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ AI Threat Detection Lab 2.1")
st.caption("Dashboard educacional de monitoramento Blue Team / SOC")

events = read_events()
df = pd.DataFrame(events)

if df.empty:
    st.info("Nenhum evento registrado ainda. Execute app.py e faça alguns testes.")
    st.stop()

total = len(df)
threats = int(df["detected"].sum())
blocked = int((df["action"] == "BLOCKED").sum())
high = int((df["severity"] == "HIGH").sum())

c1, c2, c3, c4 = st.columns(4)

c1.metric("Eventos", total)
c2.metric("Ameaças", threats)
c3.metric("Bloqueados", blocked)
c4.metric("Alta severidade", high)

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("Ameaças por tipo")
    counts = df[df["detected"]]["threat_type"].value_counts()

    if not counts.empty:
        st.bar_chart(counts)
    else:
        st.info("Nenhuma ameaça detectada.")

with right:
    st.subheader("Eventos por severidade")
    severity = df["severity"].value_counts()

    if not severity.empty:
        st.bar_chart(severity)

st.subheader("Eventos de segurança")

display_df = df[
    ["timestamp", "threat_type", "severity", "action", "input"]
].copy()

st.dataframe(
    display_df.sort_values("timestamp", ascending=False),
    use_container_width=True
)
