---
name: git-commit
description: >-
  Conventional Commits 形式でGitコミットを作成する。
  コミットしたい、git commit、変更を保存、コミットメッセージを統一したい、
  ステージされた変更をコミット、commit changes の場合に使用する。
argument-hint: "auto（自動生成）またはコミットメッセージ（例: feat: ○○機能を追加）。省略時は対話的モード。"
---

# Git Commit

## When to Use（いつ使うか）

- ステージされた変更を Conventional Commits 形式でコミットしたいとき（git commit、コミット）
- コミットメッセージを統一してリポジトリ履歴を整理したいとき
- コミット前に対象ファイルを確認してから保存したいとき（commit changes、変更を保存）

## Procedure（手順）

> **重要事項（必ず守ること）:**
> - `git commit -m` は必ずユーザーの `y` 確認後にのみ実行する
> - 確認をスキップしてコミットしてはいけない
> - コミットメッセージは **日本語・スコープなし** で記述する（形式: `<type>: <説明>`）
> - 各ステップを順番どおりに実行し、飛ばしてはいけない

### 1. 入力に応じてパターンを選択する

- `auto` → パターンA（自動生成）
- `<コミットメッセージ>` あり → パターンB（検証・実行）
- 引数なし → パターンC（対話的モード）

### 2. パターンA: 自動生成

1. 以下を**1回のターミナル呼び出し**でまとめて実行する:
   ```bash
   git add -A; git status --porcelain && git diff --staged
   ```
2. 出力を分析してコミットメッセージを自動生成する（50文字以内）:
   - 追加ファイルあり → `feat: ○○を追加`
   - 修正ファイルのみ → `fix: ○○を修正` / `refactor: ○○を整理` / `chore: ○○を更新`
   - ドキュメントのみ → `docs: ○○を更新`
3. Output Format の「自動生成確認画面」を表示してユーザーの承認を得る
4. `y` → コミット実行 / `n` → キャンセル（`git reset HEAD` でステージを戻す） / `e` → メッセージ編集

### 3. パターンB: 検証・実行

1. 入力メッセージを解析し、`type` と `description` を抽出する
2. 以下の検証項目をすべてチェックする:
   - **Type**: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `chore` のいずれか
   - **Scope**: 使用しない（`()` 不要）
   - **Description**: 日本語・50文字以下・ピリオドなし
3. 検証成功 → Output Format の「検証済み確認画面」を表示してユーザーの承認を得る
4. 検証失敗 → エラー内容と修正案を表示して終了する

### 4. パターンC: 対話的モード

1. コミットタイプを選択させる（feat / fix / docs / style / refactor / perf / test / chore）
2. 日本語の説明を入力させる（最大50文字）
3. 生成したメッセージを表示し、Output Format の「対話的確認画面」でユーザーの承認を得る
4. `y` → コミット実行

## Output Format（出力形式）

**自動生成確認画面（パターンA）:**
```
コミット対象ファイル：
  - src/pages/login.tsx
  - src/components/LoginForm.tsx

feat: ログインフォームのバリデーションを追加

[y/n/e]  y: 実行  n: キャンセル  e: メッセージ編集
```

**検証済み確認画面（パターンB）:**
```
フォーマット検証完了: feat: ログインフォームのバリデーションを追加

実行してもよろしいですか? [y/n]
```

**検証エラー:**
```
検証エラー:
  - Description が55文字です（最大50文字）

修正して再度実行してください:
  git commit feat: エラーメッセージの文字数を修正
```

**対話的確認画面（パターンC）:**
```
以下でコミットします:
  feat: ログインフォームのバリデーションを追加

実行してもよろしいですか？ [y/n]
```

**成功時:**
```
コミット完了: feat: ログインフォームのバリデーションを追加 (abc1234)

次のステップ:
  - git push でリモートにプッシュ
  - git-pull-request スキルで PR を作成
```

## References（参照）

- [Conventional Commits 仕様](https://www.conventionalcommits.org/ja/v1.0.0/)
- プロジェクトのコミット規約: `.github/copilot-instructions.md`
- PR 作成スキル: `.github/skills/git-pull-request/SKILL.md`
