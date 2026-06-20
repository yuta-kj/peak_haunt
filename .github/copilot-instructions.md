# Peak Haunt プロジェクト ガイドライン

GitHub Copilot を使用する際のプロジェクト固有のガイドラインです。このファイルは自動的にコンテキストに含まれ、Copilot の提案を統一します。

## 言語設定

プロンプトの出力は日本語で行ってください。

## プロジェクト概要

- フロントエンド: Next.js 14+ (TypeScript) - `frontend/` ディレクトリ
- バックエンド: FastAPI (Python) - `backend/` ディレクトリ
- データベース: PostgreSQL (Docker Compose 経由)
- インフラ: Docker Compose で全サービスを管理

## コーディング規則

### 全般
- 言語: フロントエンド は TypeScript、バックエンド は Python 3.11+
- 自動フォーマット: Prettier (フロントエンド)、Black (バックエンド)
- エディタ: VS Code との統合を想定

### フロントエンド (Next.js / TypeScript)
- フレームワーク: Next.js 14+ (app router)
- UI コンポーネント: `components/` ディレクトリに配置
- 再利用可能ロジック: `lib/` ディレクトリに配置
- API 呼び出し: `actions/` ディレクトリで Server Actions を使用
- スキーマ: `schemas/` ディレクトリに Zod スキーマを定義
- 命名規則:
  - コンポーネント: `PascalCase` (例: `ChatWindow.tsx`)
  - ファイル: `kebab-case` または `camelCase`
  - 関数・変数: `camelCase`

### バックエンド (FastAPI / Python)
- フレームワーク: FastAPI
- コーディング規約: PEP 8 に準拠、Black で自動フォーマット
- ルーター: `app/api/routes/` 下に配置
- 命名規則:
  - モジュール・ファイル: `snake_case`
  - 関数・変数: `snake_case`
  - クラス: `PascalCase`
  - 定数: `UPPER_SNAKE_CASE`
- パッケージ管理: `pyproject.toml` 使用

## Git コミットルール

Conventional Commits 形式を必ず使用してください。

形式: `<type>(<scope>): <subject>`

### type の種類
- `feat`: 新機能の追加
- `fix`: バグ修正
- `docs`: ドキュメント更新
- `style`: コードスタイル変更（機能変更なし）
- `refactor`: リファクタリング
- `perf`: パフォーマンス改善
- `test`: テスト追加・変更
- `chore`: ビルドプロセス・依存関係更新など
- `ci`: CI/CD 設定変更

### scope の例
- `frontend`: Next.js アプリケーション全般
- `backend`: FastAPI アプリケーション全般
- `api`: API エンドポイント
- `db`: データベース関連
- `docker`: Docker/Docker Compose

### 例
```
feat(frontend): add chat window component
fix(api): handle file upload timeout
docs(readme): update setup instructions
```

## ディレクトリ構造

```
peak_haunt/
├── .github/           # GitHub 設定・スキル・ワークフロー
├── backend/           # FastAPI バックエンド
│   ├── main.py        # エントリーポイント
│   ├── pyproject.toml # Python プロジェクト設定
│   ├── Dockerfile     # コンテナ定義
│   ├── app/           # FastAPI アプリケーション
│   │   ├── api/       # API パッケージ
│   │   │   └── routes/ # API ルーター
│   │   │       ├── chat.py
│   │   │       ├── files.py
│   │   │       └── tasks.py
│   │   └── __init__.py
│   ├── tests/         # テスト
│   └── utils/         # ユーティリティ
├── frontend/          # Next.js フロントエンド
│   ├── app/           # App Router ページ・レイアウト
│   ├── components/    # React コンポーネント
│   ├── lib/           # ユーティリティ・ヘルパー
│   ├── actions/       # Server Actions
│   ├── schemas/       # Zod スキーマ
│   ├── public/        # 静的アセット
│   ├── package.json   # Node.js 依存関係
│   ├── tsconfig.json  # TypeScript 設定
│   ├── next.config.js # Next.js 設定
│   └── Dockerfile     # コンテナ定義
└── docker-compose.yml # 開発環境定義
```

## 開発ワークフロー

1. ブランチ作成: 機能ごとに feature ブランチを作成
   ```bash
   git checkout -b feat/feature-name
   ```

2. コミット: Conventional Commits 形式で定期的にコミット
   - スキル `git-commit` を使用可能

3. プルリクエスト: 完成後は PR を作成
   - スキル `git-pull-request` を使用可能
   - タイトル・説明も Conventional Commits 形式に統一

4. マージ: レビュー後に main にマージ

## 使用可能なスキル

このリポジトリには以下の Copilot スキルが定義されています：

- `git-commit`: Conventional Commits 形式でコミット
- `git-pull-request`: PR 作成時の自動生成
- `skill-generator`: 新規スキル作成

## テスト

- フロントエンド: Jest を使用
- バックエンド: pytest を使用

テスト実行時は、それぞれのディレクトリで `npm test` または `pytest` を実行してください。

## Docker Compose

開発環境の起動：
```bash
docker compose up -d
```

全サービス（フロントエンド、バックエンド、DB）が起動します。

## その他の注意事項

- 環境変数: `.env.local` (フロントエンド)、`.env` (バックエンド) で管理
- API ベースURL: バックエンド既定値は `http://localhost:8000`
- フロントエンド ポート: 既定値 `http://localhost:3000`
- ドキュメント: 重要な決定事項は `IMPLEMENTATION_PLAN.md` に記録
