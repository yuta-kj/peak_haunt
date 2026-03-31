# peak_haunt

筋トレアプリ向けのモノレポひな形です。  
以下の要件をベースに最小構成を作成しています。

- フロントエンド: React + Next.js
- バックエンド: FastAPI
- インフラ: サーバーレス設計 (AWS Lambda / API Gateway)
- DB: PostgreSQL + pgvector
- ローカル運用: Docker Compose
- 設計思想: Clean Architecture 風に `app`, `application`, `database` を分離

## ディレクトリ構成

```text
.
├── app/
│   └── frontend/                 # Next.js
├── application/
│   └── backend/
│       └── src/
│           ├── app/              # Presentation layer (FastAPI router)
│           ├── application/      # Use cases
│           └── database/         # Repository / DB session / SQL
├── infra/
│   └── lambda/
│       └── template.yaml         # AWS SAM template
├── docker-compose.yml
└── .env.example
```

## ローカル起動

```bash
cp .env.example .env
docker compose up --build
```

起動後:

- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- Health API: http://localhost:8000/api/v1/health

## サーバーレスデプロイの足場

`infra/lambda/template.yaml` は AWS SAM 用のひな形です。  
本番では以下を調整してください。

- `DATABASE_URL` を RDS/Aurora PostgreSQL へ接続する値に変更
- VPC/Subnet/Security Group 設定を Function に追加
- CI/CD で `sam build` / `sam deploy` を組み込み

## 補足

- `application/backend/src/database/sql/init.sql` で `pgvector` 拡張を有効化
- 現在のヘルスチェックは最小実装です。今後、トレーニング記録や推薦機能を `application` と `database` に拡張できます
