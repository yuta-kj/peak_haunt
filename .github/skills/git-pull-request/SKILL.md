---
name: git-pull-request
description: "GitHub Pull Request を Conventional Commits 形式に則りながら作成します。使用方法：PR を作成したい、PR のタイトル・説明を統一したい、自動生成で効率化したい場合に使用できます。"
argument-hint: "オプション：-a [basebranch] で自動生成モード（例：-a main）、-b で タイトル指定（例：-b feat(auth): add validation）"
---

# Git Pull Request

GitHub Pull Request 作成を自動検証・自動生成で効率化します。

## クイックスタート

自動生成モード（推奨、デフォルトベースブランチ develop）：
```
git pull request
```

自動生成+ベースブランチ指定:
```
git pull request main
```


## 使用場面

- 新機能・バグ修正をコミット後、効率的に PR を作成したい
- PR タイトル・説明を統一してレビューフローを整理したい
- PR 作成前にブランチ・プッシュ状態を確認したい

## 処理フロー

### 1. リポジトリ状態を確認

PR 作成前にリポジトリの状態を確認します：

1. 現在のブランチ確認
   - `git branch` を実行して現在のブランチを確認
   - `main` にいないことを確認

2. ローカル変更確認
   - `git status` で未コミット変更がないか確認
   - あれば `/git commit` でコミットするよう促す

3. リモートプッシュ確認
   - ローカルブランチがリモートにプッシュされているか確認
   - されていなければプッシュを促す

### 2. AI が自動判断

ユーザーの入力に応じて以下に分岐：
- `git pull request` → ステップ3: 自動生成フロー（デフォルト: develop）
- `git pull request [basebranch]` → ステップ3: 自動生成フロー（develop/main 指定）


### 3. 自動生成フロー

コマンドを実行した場合、最新コミットから自動的に PR を作成します:

#### 3.1 ベースブランチ検証

引数があればベースブランチを検証：
- 有効な値: `develop`, `main`
- 無効な値: エラーメッセージ表示 → 実行キャンセル
- 省略時: デフォルト `develop` を使用

#### 3.2 最新コミット情報取得

現在のブランチの最新コミットメッセージを取得：
- Conventional Commits 形式なら type, scope, description を抽出
- 形式が異なればコミットメッセージから自動推測

#### 3.3 PR タイトル生成

コミット情報から PR タイトルを生成：
- Conventional Commits 形式の場合: `feat(auth): add login form validation` をそのまま使用
- その他の形式: 最初の50文字を採用

#### 3.4 最終確認画面

```
現在のブランチ: feature/auth-validation
ターゲットブランチ: develop

AIが最新コミットから自動生成：

feat(auth): add login form validation

この内容で PR を作成しますか? [y/n/e/d]
  y: PR 作成実行
  n: キャンセル
  e: タイトルを編集
  d: 説明を追加
```

- `y`: PR 作成実行
- `n`: キャンセル
- `e`: タイトルを編集してから確認
- `d`: 説明（description）を追加入力

### 4. エラーハンドリング

以下のエラーケースを想定：

#### 5.1 ローカル変更が未コミット
```
エラー: ローカルに未コミット変更があります

以下を実行してください：
  /git commit [メッセージ]

その後、再度実行してください：
  /git pull request
```

#### 5.2 ブランチが未プッシュ
```
警告: ローカルブランチがリモートにプッシュされていません

以下を実行してください：
  git push -u origin <ブランチ名>

その後、再度実行してください：
  /git pull request
```

#### 5.3 main ブランチから PR 作成
```
警告: main ブランチから PR を作成しようとしています

これは通常、避けるべき操作です。

本当に main から PR を作成しますか？ [y/n]
```

#### 5.4 同一ブランチで PR 既存
```
警告: 現在のブランチ（feature/auth-validation）には既に以下の PR があります：

  #123 - feat(auth): add login form validation [OPEN]

新しい PR を作成しますか？ [y/n]
```

### 5. 完了画面

PR 作成成功時：
```
PR 作成完了！

PR URL: https://github.com/yuta-kj/peak_haunt/pull/123
ブランチ: feature/auth-validation → develop
タイトル: feat(auth): add login form validation

次のステップ：
  - CI/CD パイプラインの実行を確認
  - コードレビュー者にレビューをリクエスト
  - git push で新しいコミットを追加する場合は自動で PR に反映
```

PR 作成失敗時：
```
エラー: PR 作成に失敗しました

原因: [GitHub API エラーメッセージ]

対応策：
  - ネットワーク接続を確認
  - GitHub トークンが有効か確認
  - 権限があるか確認
```
