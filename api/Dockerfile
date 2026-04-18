FROM python:3.11-slim

WORKDIR /usr/src/app

# アプリケーションコードをコピー
COPY . .

# 依存関係をインストール
RUN pip install --no-cache-dir fastapi uvicorn[standard] 2>&1 || true

# ポート 8000 を公開
EXPOSE 8000

# アプリケーションを起動
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
