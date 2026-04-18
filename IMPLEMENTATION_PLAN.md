# RAGベースの筋トレアプリ — 実装計画書

## プロジェクト要件
- **LLM**: Ollama（ローカル・無料） → 将来的にOpenAIへ切り替え可能
- **埋め込みモデル**: 無料（Hugging Face等） → 切り替え可能
- **スコープ**: 最小MVP（トレーニング記録 → RAG推奨）
- **設計**: プラガブル・プロバイダパターン

---

## フェーズ構成とタスク

### フェーズ 1: 要件・設計（1-2日）

| タスク | 内容 | 出力物 |
|-------|------|--------|
| 1-1. MVP要件定義 | ユースケース: トレーニング記録入力 → RAGで次の提案を生成 | `docs/requirements.md` |
| 1-2. データモデル設計 | ユーザ、トレーニング記録、推奨履歴 | `docs/schema.md` / ER図 |
| 1-3. プロバイダ設計 | LLM/Embedding の抽象化インターフェース | `docs/provider_design.md` |
| 1-4. アーキテクチャ図 | 全体構成（Ollama, pgvector, FastAPI, Next.js） | `docs/architecture.md` / 図 |

### フェーズ 2: 環境準備（2-3日）

| タスク | 内容 | 出力物 |
|-------|------|--------|
| 2-1. Docker Composeに Ollama追加 | ローカル LLM サーバ起動 | `docker-compose.yml` 更新 |
| 2-2. PostgreSQL スキーマ | pgvector 拡張 + テーブル定義 | `api/database/sql/init.sql` |
| 2-3. Python依存パッケージ | FastAPI, langchain, pgvector等 | `api/pyproject.toml` |
| 2-4. 埋め込みモデル準備 | sentence-transformers (all-MiniLM-L6-v2) ダウンロード・キャッシュ | `docker/requirements-embedding.txt` |

### フェーズ 3: プロバイダ層実装（3-4日）

| タスク | 内容 | 出力物 |
|-------|------|--------|
| 3-1. LLMプロバイダインターフェース | abstract base class 定義 | `api/src/providers/__init__.py` + `api/src/providers/base.py` |
| 3-2. Ollama プロバイダ実装 | OllamaProvider クラス | `api/src/providers/ollama.py` |
| 3-3. OpenAI プロバイダ実装（スタブ） | OpenAIProvider クラス（将来対応） | `api/src/providers/openai.py` |
| 3-4. Embeddingプロバイダインターフェース | abstract base class | `api/src/providers/embedding_base.py` |
| 3-5. HuggingFace埋め込みプロバイダ実装 | HFEmbeddingProvider クラス | `api/src/providers/hf_embedding.py` |
| 3-6. プロバイダ初期化・設定 | 環境変数 / Config管理 | `.env.example` 更新 + `api/src/config.py` |

### フェーズ 4: 最小MVP実装（5-7日）

| タスク | 内容 | 出力物 |
|-------|------|--------|
| 4-1. ユーザー認証API | FastAPI ベース認証 | `api/src/routes/auth.py` |
| 4-2. トレーニング記録API | POST /training-logs エンドポイント | `api/src/routes/training.py` |
| 4-3. 埋め込み生成・保存パイプライン | トレーニング記録 → 埋め込みベクトル → pgvector保存 | `api/src/services/embedding_service.py` |
| 4-4. ベクトル検索実装 | 過去記録との類似度検索 | `api/src/services/vector_search.py` |
| 4-5. プロンプトテンプレート設計 | RAG文脈 + LLMへのインストラクション | `api/src/prompts/recommendation.py` |
| 4-6. RAGチェーン実装 | 検索結果 + プロンプト → LLM生成 | `api/src/services/rag_chain.py` |
| 4-7. 推奨API | POST /recommend エンドポイント | `api/src/routes/recommendation.py` |

### フェーズ 5: フロントエンド基本UI（4-5日）

| タスク | 内容 | 出力物 |
|-------|------|--------|
| 5-1. ログイン・登録ページ | 認証フロー | `application/app/auth/` |
| 5-2. トレーニング記録フォーム | 日付、種目、セット数、重量等入力 | `application/app/training/record.tsx` |
| 5-3. 推奨結果表示 | LLMの推奨をカード形式で表示 | `application/app/training/recommendation.tsx` |
| 5-4. 記録履歴表示 | 過去記録一覧 | `application/app/training/history.tsx` |

### フェーズ 6: テスト・検証（3-4日）

| タスク | 内容 | 出力物 |
|-------|------|--------|
| 6-1. API ユニットテスト | pytest で各エンドポイントテスト | `api/tests/test_*.py` |
| 6-2. RAG品質テスト | 推奨の妥当性を手動確認 / スコア記録 | `api/tests/test_rag_quality.py` + `docs/rag_eval.md` |
| 6-3. E2E テスト | Selenium / Cypress で画面フロー確認 | `application/tests/e2e/` |
| 6-4. 性能テスト | 埋め込み生成・検索速度計測 | `docs/performance.md` |

### フェーズ 7: ドキュメント・運用準備（2-3日）

| タスク | 内容 | 出力物 |
|-------|------|--------|
| 7-1. セットアップガイド | Ollama + 本プロジェクトのセットアップ手順 | `docs/SETUP.md` |
| 7-2. プロバイダ切り替えガイド | OllamaからOpenAIへ移行する手順 | `docs/PROVIDER_SWITCH.md` |
| 7-3. 環境設定リファレンス | .env 説明、設定値一覧 | `docs/ENV_REFERENCE.md` |
| 7-4. API ドキュメント | Swagger / OpenAPI 生成確認 | `http://localhost:8000/docs` |

### フェーズ 8: デプロイ（オプション・将来）

| タスク | 内容 | 出力物 |
|-------|------|--------|
| 8-1. Lambda化（Ollama呼び出し用） | API Gateway + Lambda 設定 | `infra/lambda/template.yaml` |
| 8-2. CloudWatch ログ・監視設定 | メトリクス・アラーム定義 | `infra/monitoring/` |
| 8-3. CI/CD パイプライン | GitHub Actions で test + deploy | `.github/workflows/` |

---

## 実装の進め方

### 推奨進行順序
1. **フェーズ1 + 2** を同時並行（設計とセットアップ）
2. **フェーズ3** で抽象化層を固める ← **重要：将来の切り替えを保証**
3. **フェーズ4** で最小MVPを実装
4. **フェーズ5** でUI
5. **フェーズ6** でテスト・品質確保

### プロバイダ設計のポイント

```python
# api/src/providers/base.py (抽象化層)
from abc import ABC, abstractmethod

class LLMProvider(ABC):
    @abstractmethod
    async def generate(self, prompt: str) -> str:
        pass

class EmbeddingProvider(ABC):
    @abstractmethod
    async def embed(self, text: str) -> List[float]:
        pass

# api/src/config.py (工場関数)
def get_llm_provider() -> LLMProvider:
    provider_type = os.getenv("LLM_PROVIDER", "ollama")
    if provider_type == "ollama":
        return OllamaProvider()
    elif provider_type == "openai":
        return OpenAIProvider()
    else:
        raise ValueError(f"Unknown LLM provider: {provider_type}")
```

### 環境変数イメージ

```bash
# .env (開発)
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://ollama:11434

EMBEDDING_PROVIDER=huggingface
HF_MODEL_NAME=sentence-transformers/all-MiniLM-L6-v2

# .env (本番予定)
LLM_PROVIDER=openai
OPENAI_API_KEY=sk-xxxxx

EMBEDDING_PROVIDER=openai
OPENAI_EMBEDDING_MODEL=text-embedding-3-small
```

---

## 見積もり
- **総工数**: 約 3-4 週間（フェーズ1-6）
- **最小MVPまで**: 約 2 週間（フェーズ1-4）
- **チーム**: 1-2 人で想定

---

## 次のステップ
1. フェーズ1 → 要件書・設計書を詳細化
2. フェーズ2 → LocalOllama + Docker Compose 統合テスト
3. フェーズ3 → プロバイダ設計実装開始
