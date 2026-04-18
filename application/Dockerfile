FROM node:18-alpine

WORKDIR /usr/src/app

# アプリケーションコードをコピー
COPY . .

# 依存関係をインストール
RUN npm install --legacy-peer-deps

# Next.js をビルド
RUN npm run build

# ポート 3000 を公開
EXPOSE 3000

# アプリケーションを起動
CMD ["npm", "start"]
