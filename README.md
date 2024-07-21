# langchain

Sample Code for ChatGPT/LangChain Web Applications

## Environment Setup

> conda create -n langchain python=3.11

> pip install openai==1.35.13  
> pip install langchain==0.2.7  
> pip install langchain-community==0.2.7  
> pip install streamlit==1.36.0  

## OpenAI API Key

Create a secrets.toml file in the .streamlit folder and add the following code:

> OPENAI_API_KEY = "xxxxxxxx"  

## Execution

> conda activate langchain    
> streamlit run chatbot.py  

## Reference

[LangChain GitHub Repository](https://github.com/langchain-ai/langchain)

[サクッと始めるプロンプトエンジニアリング【LangChain / ChatGPT】](https://zenn.dev/umi_mori/books/prompt-engineer)
