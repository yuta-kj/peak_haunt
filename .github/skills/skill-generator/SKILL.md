---
name: skill-generator
description: >-
  新しい SKILL.md スキルのテンプレートとディレクトリ構造を自動生成する。
  スキルを一から作りたい、new skill、スキル作成、既存スキルと統一された構造で開発したい、
  スキルのファイル構成を効率化したい場合に使用する。
argument-hint: "スキル名（例: database-migration）とカテゴリ（例: devops）を指定する。省略時は対話的に収集。"
---

# Skill Generator

## When to Use（いつ使うか）

- 新しいスキルを一から作成したいとき（new skill、スキル作成、スキルを追加）
- `git-commit` や `git-pull-request` と統一された構造で開発したいとき
- SKILL.md のファイル構成・テンプレートを効率化したいとき

## Procedure（手順）

### 1. スキル情報を収集する

以下の情報をユーザーに確認する（引数で指定済みの場合はスキップ）:

| 項目 | 形式 | 例 |
|---|---|---|
| スキル名 | lowercase-with-hyphens（1〜64文字） | `database-migration` |
| カテゴリ | 単語（git / devops / automation など） | `devops` |
| 説明 | 「何を」+「いつ使うか」を含む1〜3文 | `DBマイグレーションを管理する。migrate、DB更新の依頼で使用する。` |

### 2. ディレクトリ構造を生成する

以下の構造で `.github/skills/<skill-name>/` を作成する:

```
.github/skills/<skill-name>/
├── SKILL.md          スキル定義（必須）
└── references/       詳細参照情報（任意）
    └── overview.md
```

### 3. SKILL.md テンプレートを生成する

収集した情報をもとに以下の形式で SKILL.md を生成する:

```yaml
---
name: <skill-name>
description: >-
  <何をするか>。
  <トリガーワード（日本語・英語）>の場合に使用する。
argument-hint: "<引数の説明>"
---

# <Skill Name>

## When to Use（いつ使うか）

- <使用場面1>
- <使用場面2>

## Procedure（手順）

1. <ステップ1>
2. <ステップ2>

## Output Format（出力形式）

<出力テンプレート>

## References（参照）

- <関連ファイル・リンク>
```

### 4. プレビューを表示してユーザーの承認を得る

Output Format の「確認画面」を表示し、`y` で `.github/skills/` に配置する。

## Output Format（出力形式）

**確認画面:**
```
生成するスキル: <skill-name>
配置先: .github/skills/<skill-name>/SKILL.md

この内容で生成しますか? [y/n/e]
  y: 生成実行
  n: キャンセル
  e: 情報を編集
```

**成功時:**
```
スキル生成完了！
作成ファイル: .github/skills/<skill-name>/SKILL.md

次のステップ:
  - SKILL.md の description にトリガーワードを追加する
  - Copilot に「<スキル名>を使って」と入力して動作確認する
```

## References（参照）

- [SKILL.md フォーマット仕様](https://agentskills.io/specification)
- [Conventional Commits](https://www.conventionalcommits.org/ja/v1.0.0/)
- 既存スキルの参考実装: `.github/skills/git-commit/SKILL.md`
