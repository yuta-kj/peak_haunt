# peak_haunt

筋トレアプリ向けのモノレポひな形です。  
以下の要件をベースに最小構成を作成しています。

- フロントエンド: React + Next.js
- バックエンド: FastAPI
- インフラ: サーバーレス設計 (AWS Lambda / API Gateway)
- DB: PostgreSQL + pgvector
- ローカル運用: Docker Compose
- 設計思想: Clean Architecture 風に `api`, `application`, `database` を分離

## ディレクトリ構成

```text
.
├── api/                          # FastAPI / Python 側の実装
│   ├── pyproject.toml
│   ├── databse/                  # DB 関連 (現状のディレクトリ名)
│   ├── tests/
│   └── utils/
├── application/                  # Next.js 側の実装
│   ├── Dockerfile
│   ├── package.json
│   ├── tsconfig.json
│   ├── actions/
│   ├── app/
│   ├── components/
│   ├── lib/
│   ├── public/
│   └── schemas/
├── database/
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

## 補足

- この README の構成図は、現在のルート直下ディレクトリ構成に合わせて更新しています
- 現在のヘルスチェックは最小実装です。今後、トレーニング記録や推薦機能を `api` と `database` に拡張できます
