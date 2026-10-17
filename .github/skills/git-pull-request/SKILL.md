---
name: git-pull-request
description: >-
  GitHub Pull Request を Conventional Commits 形式に則りながら作成する。
  PR を作成したい、pull request、プルリクエスト、PR のタイトル・説明を統一したい、
  コミット後にレビューへ提出したい、レビュー提出、open a pull request の場合に使用する。
argument-hint: "[basebranch] でベースブランチを指定（例: main）。省略時は develop。"
---

# Git Pull Request

## When to Use（いつ使うか）

- 機能開発・バグ修正のブランチで PR を作成したいとき（pull request、プルリクエスト）
- PR タイトル・説明を Conventional Commits 形式に統一したいとき
- コミット後すぐにレビューへ提出したいとき（レビュー提出、open a pull request）
- PR 作成前にブランチ・プッシュ状態を自動確認してほしいとき

## Procedure（手順）

### 1. リポジトリ状態を確認する

1. `git branch` で現在のブランチを確認し、`main` でないことを確かめる
   - `main` の場合: 警告を表示し、続行するか確認する
2. `git status` で未コミット変更がないか確認する
   - 未コミット変更がある場合: `git-commit` スキルでコミットするよう促してから終了する
3. ローカルブランチがリモートにプッシュ済みか確認する
   - 未プッシュの場合: `git push -u origin <ブランチ名>` を促してから終了する

### 2. ベースブランチを決定する

- 引数あり（例: `main`）→ その値をベースブランチに使用する
- 引数なし → デフォルト `develop` を使用する
- 有効値: `develop`, `main` のみ。それ以外はエラーを表示してキャンセルする

### 3. 最新コミットから PR タイトルを生成する

1. `git log -1 --pretty=%B` で最新コミットメッセージを取得する
2. Conventional Commits 形式（`type(scope): description`）なら、そのままタイトルに使用する
3. 形式が異なる場合は先頭 50 文字を採用する

### 4. 確認画面を表示してユーザーの承認を得る

```
現在のブランチ: feature/auth-validation
ターゲットブランチ: develop

PR タイトル（最新コミットから自動生成）:
  feat(auth): add login form validation

この内容で PR を作成しますか? [y/n/e/d]
  y: PR 作成実行
  n: キャンセル
  e: タイトルを編集
  d: 説明（body）を追加入力
```

### 5. PR を作成して結果を表示する

- 成功時: PR の URL・ブランチ名・タイトルを表示する（Output Format 参照）
- 既存 PR がある場合: PR 番号とタイトルを表示し、新規作成するか確認する
- 失敗時: エラー原因と対処策を日本語で表示する

## Output Format（出力形式）

**成功時:**
```
PR 作成完了！

PR URL: https://github.com/<owner>/<repo>/pull/<number>
ブランチ: <head> → <base>
タイトル: <title>

次のステップ：
  - CI/CD パイプラインの実行を確認
  - コードレビュー者にレビューをリクエスト
```

**警告（未コミット変更）:**
```
エラー: ローカルに未コミット変更があります
→ git-commit スキルでコミット後、再度実行してください
```

**警告（未プッシュ）:**
```
警告: ローカルブランチがリモートにプッシュされていません
→ git push -u origin <ブランチ名> を実行後、再度実行してください
```

**失敗時:**
```
エラー: PR 作成に失敗しました
原因: [GitHub API エラーメッセージ]
対処: ネットワーク接続・GitHub トークンの有効性・リポジトリ権限を確認してください
```

## References（参照）

- [Conventional Commits 仕様](https://www.conventionalcommits.org/ja/v1.0.0/)
- プロジェクトのコミット規約: `.github/copilot-instructions.md`
- コミット作成スキル: `.github/skills/git-commit/SKILL.md`
