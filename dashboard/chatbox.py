# SAFE-ALERT-AI — Module Chatbox IA
import streamlit as st


def render_chatbox(lang: str = "fr"):
    """Affiche le module chatbot d'aide à la décision."""
    st.subheader("💬 Assistant IA" if lang == "fr" else "💬 AI Assistant")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    if prompt := st.chat_input("Posez votre question..." if lang == "fr" else "Ask your question..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Réponse IA — à connecter au modèle
        response = "Fonctionnalité en cours d'intégration."
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)
