import streamlit as st
import pandas as pd
import numpy as np
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Alexandros Chrysogelos | AI/ML Engineer", page_icon="⚙️", layout="wide")

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Alexandros Chrysogelos")
st.sidebar.caption("A.I. / M.L. Engineer")

page = st.sidebar.radio("Navigation", ["🏠 Executive Summary", "🚀 MLOps & Projects", "🎓 Academic Theses", "📊 Live Inference Demo", "☕ Beyond the Code"])

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
    I don't just train models; I build the robust, secure, and scalable infrastructure required to serve them in production environments.
    """)
    
    # Quick Metrics Flex
    col1, col2, col3, col4 = st.columns(4)
    col1.metric(label="Open Source PRs", value="1", delta="Merged")
    col2.metric(label="ML Models Deployed", value="15+")
    col3.metric(label="Tech Stack", value="Python, Docker", delta="FastAPI, PyTorch")
    col4.metric(label="Current Status", value="KU Leuven", delta="Adv. Master in AI")

    st.divider()
    
    # Resume Section
    st.header("💼 Experience")
    st.markdown("**A.I./M.L. Engineer @ Unisystems (Athens)** | *Oct 2025 - Present*")
    st.markdown("- Developing the 'Uniqprovals' internal platform using SPFX, React, and TypeScript.")
    st.markdown("- Implementing chatbot solutions and leveraging AI tools to boost efficiency and accelerate delivery.")
    
    st.markdown("**Research and Technology Center @ Hellenic Military** | *Nov 2023 - May 2024*")
    st.markdown("- Developed ML algorithms for autonomous naval systems and enhanced stealth radar with signal processing.")
    
    st.markdown("**IT Intern @ Stavros Niarchos Foundation** | *April - July 2023*")
    st.markdown("- Contributed to Azure cloud infrastructure administration and implemented cybersecurity patches.")
    
    st.header("🎓 Education")
    st.markdown("- **Advanced Master in Artificial Intelligence** - KU Leuven (Oct 2024 - Jan 2026)")
    st.markdown("- **MSc in Computer Engineering & Informatics (GPA: 7.2/10)** - University of Patras (Oct 2017 - Aug 2023)")

# --- PAGE 2: MLOPS & PROJECTS ---
elif page == "🚀 MLOps & Projects":
    st.title("⚙️ Engineering & Open Source Projects")
    st.markdown("A selection of my end-to-end Machine Learning pipelines and architectural deployments.")
    
    with st.expander("🏆 Vault AI: Enterprise Multi-Tenant RAG SaaS", expanded=True):
        st.markdown("**[🔗 GitHub Repository](https://github.com/alexchrys99/vault-ai)**")
        st.markdown("""
        * Architected a fully local, containerized RAG application using Meta's Llama 3.2 via Ollama and ChromaDB, ensuring zero data leakage.
        * Implemented Row-Level Security via vector metadata tagging and built a secure authentication system using FastAPI, SQLite, and Bcrypt.
        * Orchestrated a microservice architecture using Docker Compose and shared-base images, integrating a stateful Streamlit frontend with LangChain conversational memory.
        """)

    with st.expander("📈 ETF Hedge Fund AI: End-to-End MLOps"):
        st.markdown("**[🔗 GitHub Repository](https://github.com/alexchrys99/etf-mlops)**")
        st.markdown("""
        * Designed a PyTorch Transformer ensemble (5 models) predicting market movements using price action and FinBERT.
        * Built an automated data engineering pipeline storing financial data in Apache Parquet format.
        * Integrated MLflow for tracking and served predictions via a Dockerized FastAPI REST server.
        """)
        
    with st.expander("🏀 NBA Oracle: Hybrid AI MLOps Pipeline"):
        st.markdown("**[🔗 GitHub Repository](https://github.com/alexchrys99/nba-oracle-mlops)**")
        st.markdown("""
        * Engineered an end-to-end containerized MLOps pipeline using XGBoost and Transformers to predict sports performance.
        * Implemented CI/CD workflows using GitHub Actions for automated testing and continuous integration.
        * Deployed the inference engine as a microservice using Docker, exposing the model via FastAPI and an interactive Streamlit dashboard.
        """)

    with st.expander("🏥 MLOps Diagnostic API (XGBoost)"):
        st.markdown("**[🔗 GitHub Repository](https://github.com/alexchrys99/mlops-xgboost-api)**")
        st.markdown("""
        * Developed an XGBoost machine learning pipeline to classify clinical data with high diagnostic accuracy.
        * Packaged the inference engine in an isolated Docker container and exposed it via FastAPI for real-time serving.
        """)
        
    with st.expander("🌍 Open Source Contribution: Orallexa AI Trading Agent"):
        st.markdown("**[🔗 View Pull Request #3](https://github.com/alex-jb/orallexa-ai-trading-agent/pull/3)** *(Pending Merge)*")
        st.markdown("""
        * Engineered Docker container hardening by implementing a non-root execution environment.
        * Built an automated `curl`-based `/healthz` API endpoint to enable robust container orchestration and health tracking.
        """)

# --- PAGE 3: ACADEMIC THESES ---
elif page == "🎓 Academic Theses":
    st.title("🎓 Academic Research & Theses")
    
    st.markdown("### KU Leuven Thesis")
    st.markdown("**Preventing Unwanted Ads and Harmful Visual Media for Children**")
    st.markdown("[🔗 GitHub Repository](https://github.com/alexchrys99/KUL_thesis) | [📄 Read the Paper](https://drive.google.com/file/d/1S2AIgft1XOhQBtwxoMhYdVT16G-pThs7/view?usp=drive_link)")
    st.markdown("""
    * Implemented a client-server browser solution for real-time NSFW filtering using YOLOv11 (CNN).
    * Developed context-aware adaptive logic to optimize detection accuracy and minimize system latency.
    """)
    
    st.divider()
    
    st.markdown("### University of Patras Thesis")
    st.markdown("**NBA & WNBA Player Performance Prediction with ANN**")
    st.markdown("[🔗 View Project Files](https://drive.google.com/drive/folders/1oCMsTLClCDU1eC2C_02_aBrA9gNlUGuD?usp=sharing)")
    st.markdown("""
    * Trained Artificial Neural Networks (ANN) in Python/MATLAB predicting player performance with >85% accuracy.
    * Engineered 10+ statistical features from sports datasets to optimize model training.
    * Applied extensive hyperparameter tuning to ensure robust model generalization.
    """)

# --- PAGE 4: LIVE AI ASSISTANT ---
elif page == "📊 Live Inference Demo":  # Changed back to your preferred title, or use "🤖 Chat with my CV"
    st.title("🤖 Ask my AI Assistant")
    st.markdown("""
    Welcome to my live LLM demo! I have injected my resume and project history into the context of this AI. 
    **Go ahead, ask it about my MLOps experience, my tech stack, or my Master's degree!**
    """)
    
    import openai
    
    # 1. Set up the System Prompt (The "RAG" Context)
    system_prompt = """
    You are the professional AI assistant for Alexandros Chrysogelos. 
    Here is his background:
    - He is an A.I./M.L. Engineer specializing in MLOps, RAG, and FastAPI.
    - He works at Unisystems developing the Uniqprovals platform (React/TypeScript).
    - He has an Advanced Master in AI from KU Leuven and an MSc in Computer Engineering from Univ. of Patras.
    - Projects: Built "Vault AI" (Local RAG with Llama 3.2, ChromaDB, Docker), "NBA Oracle" (XGBoost MLOps pipeline), and contributed to "Orallexa AI" open source.
    - Tech Stack: Python, PyTorch, Docker, FastAPI, MLflow, LangChain, React, TypeScript.
    Answer questions about him professionally, concisely, and enthusiastically. Do not invent information.
    """

    # 2. Initialize Chat History in Streamlit Session State
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "system", "content": system_prompt},
            {"role": "assistant", "content": "Hi! I'm Alex's AI assistant. What would you like to know about his engineering experience?"}
        ]

    # 3. Display previous chat messages
    for msg in st.session_state.messages:
        if msg["role"] != "system": # Hide the system prompt from the UI
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    # 4. Handle User Input (No API key asked from the user!)
    if user_input := st.chat_input("E.g., What is Alex's experience with Docker?"):
        
        # Display user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # Call the FREE Groq Llama 3 API securely
        try:
            client = openai.OpenAI(
                base_url="https://api.groq.com/openai/v1",
                api_key=st.secrets["GROQ_API_KEY"] # Pulls from Streamlit Cloud Secrets
            )
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response = client.chat.completions.create(
                        model="llama-3.1-8b-instant", # The upgraded Llama 3.1 model
                        messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
                    )
                    bot_reply = response.choices[0].message.content
                    st.markdown(bot_reply)
                    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
        except Exception as e:
            st.error(f"Oops! The API key is not configured properly in Streamlit Secrets. Error: {e}")

# --- PAGE 5: ABOUT ME ---
elif page == "☕ Beyond the Code":
    st.title("☕ Beyond the Code")
    st.markdown("You can't containerize personality! Here is what I do when I am not writing Python or fighting with Linux permissions:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏀 Interests & Activities")
        st.markdown("- **Sports:** Avid NBA fan, football.")
        st.markdown("- **Fitness:** Strength training and participant in the Adidas Runners community.")
        st.markdown("- **Travel:** Regular traveler with a focus on cultural exchange.")
        st.markdown("- **Student Organizations:** Active member in BEST Patras and ESN Leuven.")
        
    with col2:
        st.subheader("🌍 Erasmus+ Projects")
        st.markdown("**Migration: Think Better, Think Critically (Poland)**")
        st.markdown("- Co-created migration policy solutions and facilitated debates alongside 30+ international participants.")
        st.markdown("- Developed intercultural communication and critical thinking skills within diverse, multicultural teams.")
        
        st.markdown("**Stay Offline (Cyprus)**")
        st.markdown("- Refined public speaking and conflict resolution skills by presenting workshop findings to European youth groups.")
