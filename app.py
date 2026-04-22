import streamlit as st
import pandas as pd
import numpy as np
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Alexandros Chrysogelos | AI/ML Engineer", page_icon="⚙️", layout="wide")

# --- SIDEBAR NAVIGATION ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/8637/8637130.png", width=100) # Placeholder for your face
st.sidebar.title("Alexandros Chrysogelos")
st.sidebar.caption("A.I. / M.L. Engineer")

page = st.sidebar.radio("System Navigation", ["🏠 Executive Summary", "🚀 MLOps & Projects", "📊 Live Inference Demo", "☕ Beyond the Code"])

st.sidebar.divider()
st.sidebar.markdown("**Contact & Links**")
st.sidebar.markdown("[LinkedIn](https://linkedin.com/in/alexchrys99) | [GitHub](https://github.com/alexchrys99)")
st.sidebar.markdown("📍 Athens, Greece")

# --- PAGE 1: HOME / RESUME ---
if page == "🏠 Executive Summary":
    st.title("Hi, I'm Alexandros 👋")
    st.subheader("I engineer production-grade AI systems.")
    
    st.markdown("""
    I am an A.I./M.L. Engineer specializing in **Machine Learning Operations (MLOps), Retrieval-Augmented Generation (RAG), and Containerized Microservices**. 
    I don't just train models in Jupyter Notebooks; I build the robust, secure, and scalable infrastructure required to serve them in production.
    """)
    
    # Quick Metrics Flex
    col1, col2, col3, col4 = st.columns(4)
    col1.metric(label="Open Source PRs", value="1", delta="Orallexa AI")
    col2.metric(label="ML Models Deployed", value="15+")
    col3.metric(label="Docker Containers", value="20+")
    col4.metric(label="Current Status", value="KU Leuven", delta="Adv. Master in AI")

    st.divider()
    
    # Resume Section
    st.header("💼 Experience")
    st.markdown("**A.I./M.L. Engineer @ Unisystems (Athens)** | *Oct 2025 - Present*")
    st.markdown("- Developing the 'Uniqprovals' internal platform using React, TypeScript, and AI tools.")
    st.markdown("**ML Researcher @ Hellenic Army R&D** | *Nov 2023 - May 2024*")
    st.markdown("- Developed autonomous naval ML algorithms and enhanced stealth radar via signal processing.")
    
    st.header("🎓 Education")
    st.markdown("- **Advanced Master in Artificial Intelligence** - KU Leuven (2024 - 2026)")
    st.markdown("- **MSc in Computer Engineering & Informatics** - University of Patras (2017 - 2023)")

# --- PAGE 2: MLOPS & PROJECTS ---
elif page == "🚀 MLOps & Projects":
    st.title("⚙️ MLOps Architecture & Projects")
    
    st.markdown("### 🏆 Vault AI: Enterprise Multi-Tenant RAG SaaS")
    st.markdown("""
    **Tech Stack:** Docker, FastAPI, Streamlit, ChromaDB, Llama 3.2, Ollama  
    * **The Problem:** Corporate data leakage to external LLM APIs.
    * **The MLOps Solution:** Architected a 100% local, containerized microservice network. Implemented **Row-Level Security** in the vector database to guarantee multi-tenant data isolation. 
    """)
    
    st.divider()
    
    st.markdown("### 🏀 NBA Oracle: Hybrid AI MLOps Pipeline")
    st.markdown("""
    **Tech Stack:** XGBoost, GitHub Actions, Docker, FastAPI  
    * **The MLOps Solution:** Engineered an end-to-end CI/CD pipeline. The inference engine is packaged in an isolated Docker container and served via a high-performance REST API.
    """)
    
    st.divider()
    
    st.markdown("### 🌍 Open Source: Orallexa AI Trading Agent")
    st.markdown("""
    **Contribution:** Merged PR #3  
    * **DevOps Security:** Engineered Docker container hardening by implementing a non-root execution environment and building an automated `curl`-based `/healthz` API endpoint for container orchestration.
    """)

# --- PAGE 3: INTERACTIVE DEMO ---
elif page == "📊 Live Inference Demo":
    st.title("📊 System Telemetry & Model Inference")
    st.markdown("As an MLOps Engineer, I care about **Model Drift** and **System Health**. Here is a simulated dashboard of an active XGBoost model in production.")
    
    st.info("💡 Try clicking the button below to 'ping' the inference server.")
    if st.button("Ping FastAPI Inference Server"):
        with st.spinner("Querying model endpoint..."):
            time.sleep(1.5)
            st.success("Response 200 OK: Prediction returned in 42ms.")
            
    # Mock MLOps Dashboard
    st.subheader("Model Latency Tracking (Last 50 Requests)")
    latency_data = pd.DataFrame(
        np.random.normal(40, 5, size=(50, 1)),
        columns=['Latency (ms)']
    )
    st.line_chart(latency_data)

# --- PAGE 4: ABOUT ME ---
elif page == "☕ Beyond the Code":
    st.title("☕ Beyond the Code")
    st.markdown("You can't containerize personality! Here is what I do when I am not writing Python or fighting with Linux permissions:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏀 Sports & Fitness")
        st.markdown("- **Avid NBA Fan:** Combining my love for basketball with data science (hence the NBA Oracle project!).")
        st.markdown("- **Strength Training & Running:** Active participant in the Adidas Runners community.")
        
    with col2:
        st.subheader("🌍 Cultural Exchange & Leadership")
        st.markdown("- **Erasmus+:** Co-created migration policy solutions in Poland and facilitated conflict resolution workshops in Cyprus.")
        st.markdown("- **Student Organizations:** Proudly active in BEST Patras and ESN Leuven, building multicultural networks.")
        st.markdown("- **Travel:** Regular traveler always looking for the next cultural exchange.")