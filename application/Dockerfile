FROM node:18-alpine AS builder

WORKDIR /app

# アプリケーションコードをコピー
COPY . .

# 依存関係をインストール
RUN npm install --legacy-peer-deps

# Next.js をビルド
RUN npm run build

# 本番イメージ
FROM node:18-alpine

WORKDIR /app

# ビルダーから .next とnode_modules をコピー
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/package.json ./package.json

# ポート 3000 を公開
EXPOSE 3000

# アプリケーションを起動
CMD ["npm", "start"]
