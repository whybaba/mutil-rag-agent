"""
应用配置管理
"""
from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """应用配置"""
    
    # ---- 应用 ----
    APP_NAME: str = "MultiAgentAIOps"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False
    HOST: str = "0.0.0.0"
    PORT: int = 9900
    
    # ---- LLM ----
    DEEPSEEK_API_KEY: Optional[str] = None
    DEEPSEEK_BASE_URL: str = "https://api.deepseek.com"
    DASHSCOPE_API_KEY: Optional[str] = None
    DASHSCOPE_BASE_URL: str = "https://dashscope.aliyuncs.com/compatible-mode/v1"
    DASHSCOPE_CHAT_MODEL: str = "deepseek-v4-pro"
    DASHSCOPE_ROUTER_MODEL: str = "deepseek-v4-flash"
    
    # ---- Embedding ----
    EMBEDDING_PROVIDER: str = "ollama"
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_EMBEDDING_MODEL: str = "bge-m3"
    OLLAMA_EMBEDDING_DIM: int = 1024
    
    # ---- Milvus ----
    MILVUS_HOST: str = "localhost"
    MILVUS_PORT: int = 19530
    MILVUS_COLLECTION: str = "multi_agent_kb"
    
    # ---- PostgreSQL ----
    DATABASE_URL: str = "postgresql://multi_agent:multi_agent@localhost:5432/multi_agent_aiops"
    
    # ---- Redis ----
    REDIS_URL: str = "redis://localhost:6379/0"
    
    # ---- RAG ----
    RAG_TOP_K: int = 3
    RAG_CHUNK_SIZE: int = 800
    RAG_CHUNK_OVERLAP: int = 100
    RAG_PARENT_MAX_CHARS: int = 2400
    RAG_HYBRID_ENABLED: bool = True
    RAG_RETRIEVE_K: int = 30
    RAG_HYBRID_BM25_WEIGHT: float = 0.4
    RAG_RERANK_ENABLED: bool = True
    RAG_RERANK_PROVIDER: str = "local"
    RAG_RERANK_MODEL: str = "BAAI/bge-reranker-v2-m3"
    
    # ---- 查询重写（新增） ----
    RAG_QUERY_REWRITE_ENABLED: bool = True
    RAG_QUERY_REWRITE_MODEL: Optional[str] = None
    
    # ---- Agent ----
    AGENT_MAX_STEPS: int = 5
    AGENT_MAX_CONCURRENCY: int = 2
    PERMISSION_MODE: str = "normal"
    
    # ---- 日志 ----
    LOG_LEVEL: str = "INFO"
    LOG_DIR: str = "logs"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


settings = Settings()