FROM python:3.11-slim

WORKDIR /usr/src/app

# アプリケーションコードをコピー
COPY . .

# PYTHONPATH を設定
ENV PYTHONPATH=/usr/src/app

# 依存関係をインストール（リトライ付き）
RUN pip install --no-cache-dir --retries 5 fastapi uvicorn[standard] || \
    pip install --no-cache-dir fastapi uvicorn[standard] || \
    echo "Warning: pip install failed, but continuing..."

# ポート 8000 を公開
EXPOSE 8000

# アプリケーションを起動
CMD ["python", "-m", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
