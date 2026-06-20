---
name: skill-generator
description: "新しいスキルを作成する際のテンプレートを自動生成します。スキル名とカテゴリを入力すると、SKILL.md、スクリプト、参考資料テンプレートを含む完全なスキルディレクトリを生成します。Use when: 新しいスキルを一から作成したい、既存スキルと統一された構造で開発したい、スキルのファイル構成を効率化したい場合に使用できます。"
argument-hint: "スキル名（例：project-setup）、カテゴリ（例：devops, automation）"
---

# Skill Generator

新しいスキルを作成する際の標準テンプレートと構造を自動生成するスキルです。

## 使用場面

- 新しいスキルを一から作成したい
- 既存スキル（git-commit など）と統一された構造で開発したい
- スキルのファイル構成を効率化したい

## 処理フロー

### 1. スキル情報を収集

以下の情報をユーザーに確認します：

- スキル名: 小文字、ハイフン区切り（例：skill-generator）
- カテゴリ: スキルの分類（例：git, development, automation）
- 説明: スキルの目的と使用場面（最大1024文字）
- タイプ: スキルの処理種類
  - workflow: 複数ステップのワークフロー
  - generator: テンプレートやコード生成
  - analyzer: 分析・検証処理
  - integrator: 外部ツール連携

### 2. ディレクトリ構造を生成

以下の構造を自動作成します：

```
.github/skills/<skill-name>/
├── SKILL.md              スキル定義（メタデータ+説明）
├── README.md             使用ガイド
├── references/
│   ├── architecture.md   アーキテクチャ説明
│   └── api-reference.md  外部APIなどの参照情報
└── assets/
    ├── templates/        生成テンプレート
    └── scripts/          実行スクリプト
```

### 3. テンプレートファイルを生成

各ファイルに以下の内容を含めます：

#### 3.1 SKILL.md
```yaml
---
name: <skill-name>
description: '<説明>'
argument-hint: '使用時のヒント'
---

# <Skill Name>
...
```

#### 3.2 README.md
クイックスタート、使用場面、詳細な処理フロー

#### 3.3 References
- architecture.md: 内部構成と処理フロー
- api-reference.md: 外部ツール・APIの仕様

#### 3.4 Assets
- templates/: テンプレートファイル集
- scripts/: 実行可能なスクリプト（Node.js、Python など）

### 4. 出力と確認

生成内容をプレビューし、ユーザーが確認後、.github/skills/ に配置します。

## 生成例

入力:
- スキル名: database-migration
- カテゴリ: devops
- 説明: Create and manage database migrations with version control

生成出力:
```
.github/skills/database-migration/
├── SKILL.md
├── README.md
├── references/
│   ├── migration-strategy.md
│   └── supported-databases.md
└── assets/
    ├── templates/
    │   ├── migration-template.sql
    │   └── rollback-template.sql
    └── scripts/
        ├── create-migration.js
        └── validate-migration.js
```

## 命名規則

- スキル名: lowercase-with-hyphens (1-64 文字)
- ファイル: 説明的でスネークケース（例：api-reference.md）
- フォルダ: templates/, scripts/, references/

参考: [スキル構造ガイド](./references/skill-structure.md) | [命名規則](./references/naming-conventions.md)
