# peak_haunt

筋トレアプリ向けのモノレポひな形です。  
以下の要件をベースに最小構成を作成しています。

- フロントエンド: React + Next.js
- バックエンド: FastAPI
- インフラ: サーバーレス設計 (AWS Lambda / API Gateway)
- DB: PostgreSQL + pgvector
- ローカル運用: Docker Compose
- 設計思想: Clean Architecture 風に `api`, `application`, `database` を分離

## 技術スタック

### Backend
- Python: 3.11以上
- フレームワーク: FastAPI
- パッケージ管理: Poetry

### Frontend
- フレームワーク: Next.js
- 言語: TypeScript

### 開発環境
- Docker Compose
- PostgreSQL + pgvector

### 品質管理
- Python Linting: ruff
- Python テスト: pytest
- TypeScript: strict モード設定


## ローカル起動

```bash
cp .env.example .env
docker compose up --build
```

起動後:

- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- Health API: http://localhost:8000/api/v1/health

## 補足

- この README の構成図は、現在のルート直下ディレクトリ構成に合わせて更新しています
- 現在のヘルスチェックは最小実装です。今後、トレーニング記録や推薦機能を `api` と `database` に拡張できます
