"""
Utility module to handle secrets for both local development and Streamlit Cloud deployment
"""
import os

def get_api_key():
    """
    Get the GROQ API key from either environment variables or Streamlit secrets
    Returns:
        str: The API key
    """
    try:
        # Try to import streamlit and get from secrets
        import streamlit as st
        if hasattr(st, 'secrets') and 'GROQ_API_KEY' in st.secrets:
            return st.secrets['GROQ_API_KEY']
    except (ImportError, Exception):
        pass
    
    # Fallback to environment variable for local development
    return os.getenv('GROQ_API_KEY')
