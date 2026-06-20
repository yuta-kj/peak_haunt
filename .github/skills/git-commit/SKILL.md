---
name: git-commit
description: "Conventional Commits形式でGitコミットを作成します。使用方法：ステージされた変更をコミットしたい、Conventional Commits形式で統一したい、コミット前にファイルを確認したい場合に使用できます。"
argument-hint: "オプション：コミットメッセージを提供すると自動検証・実行します（例：feat(auth): add login form validation）"
---

# Git Commit

Conventional Commits形式の自動検証付きでGitコミットを作成します。

## クイックスタート

自動生成モード（推奨）：
```
git commit auto
```

メッセージを指定して実行：
```
git commit feat: 新機能の説明
```

対話的に実行：
```
git commit
```

## 使用場面

- ステージされた変更をConventional Commits形式でコミットしたい
- コミットメッセージを統一してリポジトリ履歴を整理したい
- コミット前にどのファイルが含まれるか確認したい

## 処理フロー

### 1. Git ステータスを確認

コミット実行前にリポジトリの状態を確認します：

1. ステージされたファイルを確認
   - `git status` を実行してステージされたファイルが存在するか確認
   - なければユーザーに `git add` でステージするか確認
   - あれば、どのファイルがコミットに含まれるかを一覧表示

2. ファイル一覧を表示
   ```
   ステージされたファイル：
      - src/pages/login.tsx
      - src/components/LoginForm.tsx
   ```

### 2. AI が自動判断

ユーザーの入力に応じて以下に分岐：
- `git commit auto` → ステップ3: 自動生成フロー
- `git commit <メッセージ>` → ステップ4: 自動検証・実行フロー
- `git commit` → ステップ5: 対話的モード

### 3. 自動生成フロー（パターンA）

`auto` オプションが指定された場合、AIがファイル変更から自動的にコミットメッセージを生成します：

#### 3.1 変更内容を分析

ステージされたファイルの差分から：
- 追加されたファイル → 新機能 (feat)
- 修正されたファイル → バグ修正 (fix)
- ドキュメントのみ変更 → ドキュメント (docs)

#### 3.2 メッセージを生成

ファイル変更から自動的にメッセージを生成：
- 領域（auth, api, ui など）を自動判定
- 50文字以内に収める

#### 3.3 最終確認画面

```
ステージされたファイル：
   - src/pages/login.tsx
   - src/components/LoginForm.tsx

AIが変更内容から自動生成：

feat(auth): add login form validation

このメッセージでコミットしますか? [y/n/e]
  y: コミット実行
  n: キャンセル
  e: メッセージを編集
```

- `y`: コミット実行
- `n`: キャンセル
- `e`: メッセージを編集してから確認

### 4. 自動検証・実行フロー（パターンB）

完全なコミットメッセージが提供された場合：

#### 4.1 メッセージを解析
入力から以下を抽出します：
- Type: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `chore`
- Scope(オプション): 括弧内のテキスト
- Description: コロン後のテキスト

例：`feat(auth): add login form validation`
- Type: `feat`
- Scope: `auth`
- Description: `add login form validation`

#### 4.2 フォーマット検証

形式: `<type>[(<scope>)]: <description>`

**検証項目：**
- **Type**: feat, fix, docs, style, refactor, perf, test, chore のいずれか
- **Scope**（オプション）: 変更の影響を受ける領域（auth, api, ui など、小文字、1～3単語）
- **Description**: 命令形で50文字以下、最初は大文字、ピリオドなし、具体的に記述

例：
- `feat(auth): add login validation`
- `fix(api): resolve timeout error`
- `docs: update readme`

#### 4.3 検証結果に応じた処理

検証成功の場合:
```
フォーマット検証完了: feat(auth): add login form validation

実行してもよろしいですか? [y/n]
```
- ユーザーが確認 → コミット実行
- `git commit -m "feat(auth): add login form validation"`

検証失敗の場合:
```
検証エラー:
  - Description が55文字です（最大50文字）

修正して再度実行してください：
/git commit feat(auth): fix error message character count
```

### 5. 対話的モード（パターンC）

メッセージが提供されていない場合、ステップバイステップでガイドします：

#### 5.1 コミットタイプを選択
```
コミットタイプを選択してください：
  feat      - 新しい機能を追加
  fix       - バグを修正
  docs      - ドキュメント変更のみ
  style     - コード形式の変更（スペース、セミコロンなど）
  refactor  - コードの再構成（動作変わらず）
  perf      - パフォーマンス改善
  test      - テスト関連の変更
  chore     - 依存関係やビルド設定など
```

#### 5.2 Scope を入力(オプション)
```
影響を受ける領域/コンポーネント？（例：auth, api, ui）
[Enterで省略]
```

#### 5.3 Description を入力
```
簡潔な説明を命令形で入力してください（最大50文字）：
```

例：`add login form validation`

#### 5.4 最終確認
AI がメッセージを自動生成して表示：
```
以下でコミットします：

feat(auth): add login form validation

実行してもよろしいですか？ [y/n]
```

#### 5.5 コミット実行
ユーザーが確認すればコミットを実行：
```
git commit -m "feat(auth): add login form validation"
```

### 6. 完了画面

コミット成功時：
```
コミット完了: feat(auth): add login form validation (abc1234)

次のステップ：
  - git push で リモートにプッシュ
  - /create-pull-request で PR を作成
```
