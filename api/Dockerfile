# syntax=docker/dockerfile:1
FROM python:3.11-slim

WORKDIR /usr/src/app

# アプリケーションコードをコピー
COPY . .

# 依存関係をインストール
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install fastapi uvicorn[standard] || \
    (echo "Installation failed" && exit 1)

# ポート 8000 を公開
EXPOSE 8000

# アプリケーションを起動
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
