# ステージ 1: Alpine + ビルドツールで依存関係をインストール（Tailwind v4 ネイティブバインディングをコンパイル）
FROM node:18-alpine AS builder

# Tailwind v4 の Rust バインディングコンパイルに必要なツール
RUN apk add --no-cache python3 make g++

WORKDIR /usr/src/app

# package-lock.json をコピーしない（npm bug #4828 回避: ロックファイルなしで解決させる）
COPY package.json ./
RUN npm install && \
    OXIDE_VER=$(node -e "console.log(JSON.parse(require('fs').readFileSync('node_modules/@tailwindcss/oxide/package.json')).version)") && \
    npm install --no-save "@tailwindcss/oxide-linux-x64-musl@${OXIDE_VER}"

# ステージ 2: Alpine ベースの軽量イメージで本番実行（musl 互換バイナリを使用）
FROM node:18-alpine AS runner

WORKDIR /usr/src/app

# ビルドステージからコンパイル済み node_modules をコピー
COPY --from=builder /usr/src/app/node_modules ./node_modules

# アプリケーションコードをコピー
COPY . .

# ポート 3000 を公開
EXPOSE 3000

# 開発サーバーを起動（0.0.0.0 でコンテナ外からアクセス可能にする）
CMD ["npx", "next", "dev", "-H", "0.0.0.0"]
