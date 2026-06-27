FROM node:18-alpine

WORKDIR /usr/src/app

# 依存関係ファイルをコピー
COPY package.json package-lock.json* ./

# 依存関係をインストール
RUN npm install

# アプリケーションコードをコピー
COPY . .

# ポート 3000 を公開
EXPOSE 3000

# 開発サーバーを起動（0.0.0.0 でコンテナ外からアクセス可能にする）
CMD ["npx", "next", "dev", "-H", "0.0.0.0"]
