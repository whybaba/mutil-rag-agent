# ============================================================
# Multi-Agent AIOps Platform - 应用镜像 (API + Worker 共用)
# ============================================================
FROM python:3.12-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# ============================================================
# 一次性安装所有缺失的依赖（修复 ModuleNotFoundError）
# ============================================================
RUN pip install \
    sse_starlette \
    loguru \
    langchain_milvus \
    langchain \
    langchain-community \
    langchain_mcp_adapters \
    pymilvus \
    psycopg2-binary \
    httpx \
    python-dotenv \
    psutil \
    python-multipart \
    asyncpg \
    fastapi \
    uvicorn \
    pydantic \
    pydantic-settings \
    sqlalchemy \
    redis \
    aiofiles \
    pandas \
    numpy \
    tiktoken \
    tenacity \
    requests
COPY . .

EXPOSE 9900

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "9900", "--workers", "4"]