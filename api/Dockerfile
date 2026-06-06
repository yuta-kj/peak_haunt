# syntax=docker/dockerfile:1
FROM python:3.11-slim

WORKDIR /usr/src/app

# Poetryをインストール
RUN pip install --no-cache-dir poetry

# pyproject.toml と poetry.lock をコピー
COPY pyproject.toml poetry.lock* ./

# 依存関係をインストール（本番環境）
RUN poetry install --only main --no-root

# アプリケーションコードをコピー
COPY . .

# ポート 8000 を公開
EXPOSE 8000

# アプリケーションを起動
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
