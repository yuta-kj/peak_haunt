---
name: git-commit
description: "Conventional Commits形式でGitコミットを作成します。使用方法：ステージされた変更をコミットしたい、Conventional Commits形式で統一したい、コミット前にファイルを確認したい場合に使用できます。"
argument-hint: "オプション：コミットメッセージを提供すると自動検証・実行します（例：feat(auth): add login form validation）"
---

# Git Commit

Conventional Commits形式の自動検証付きでGitコミットを作成します。

## 使用場面

- ステージされた変更をConventional Commits形式でコミットしたい
- コミットメッセージを統一してリポジトリ履歴を整理したい
- コミット前にどのファイルが含まれるか確認したい
- 「コミットして」「git commit」などと言ったとき

## 処理フロー

### 1. Git ステータスを確認

コミット実行前にリポジトリの状態を確認します：

1. **ステージされたファイルを確認**
   - `git status` を実行してステージされたファイルが存在するか確認
   - なければユーザーに `git add` でステージするか確認
   - あれば、どのファイルがコミットに含まれるかを一覧表示

2. **ファイル一覧を表示**
   ```
   ✅ ステージされたファイル：
      - src/pages/login.tsx
      - src/components/LoginForm.tsx
   ```

### 2. AI が自動判断

ユーザーの入力パターンを判定して処理を振り分けます：

#### **パターンA：完全なメッセージを提供**
以下のような入力がされた場合：
```
/git-commit feat(auth): add login form validation
```

**→ ステップ3：自動検証・実行フロー に進む**

#### **パターンB：メッセージなし（対話的ガイド）**
以下のような入力がされた場合：
```
/git-commit
```

**→ ステップ4：対話的モード に進む**

### 3. 自動検証・実行フロー（パターンA）

完全なコミットメッセージが提供された場合：

#### **3.1 メッセージを解析**
入力から以下を抽出します：
- **Type**：`feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `chore`
- **Scope**（オプション）：括弧内のテキスト
- **Description**：コロン後のテキスト

例：`feat(auth): add login form validation`
- Type: `feat`
- Scope: `auth`
- Description: `add login form validation`

#### **3.2 フォーマット検証**
以下の項目をチェックします：
- ✅ Type が有効か（上記8種類のいずれか）
- ✅ 形式が `<type>[(<scope>)]: <description>` か
- ✅ Description が命令形か
- ✅ Description が50文字以下か
- ✅ 末尾にピリオドがないか

#### **3.3 検証結果に応じた処理**

**検証 ✅ 成功の場合：**
```
✅ フォーマット検証完了：feat(auth): add login form validation

実行してもよろしいですか？ [y/n]
```
- ユーザーが確認 → コミット実行
- `git commit -m "feat(auth): add login form validation"`

**検証 ❌ 失敗の場合：**
```
❌ 検証エラー：
  - Description が55文字です（最大50文字）

修正して再度実行してください：
/git-commit feat(auth): fix error message character count
```

### 4. 対話的モード（パターンB）

メッセージが提供されていない場合、ステップバイステップでガイドします：

#### **4.1 コミットタイプを選択**
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

#### **4.2 Scope を入力（オプション）**
```
影響を受ける領域/コンポーネント？（例：auth, api, ui）
[Enterで省略]
```

#### **4.3 Description を入力**
```
簡潔な説明を命令形で入力してください（最大50文字）：
```

例：`add login form validation`

#### **4.4 最終確認**
AI がメッセージを自動生成して表示：
```
以下でコミットします：

feat(auth): add login form validation

実行してもよろしいですか？ [y/n]
```

#### **4.5 コミット実行**
ユーザーが確認すればコミットを実行：
```
git commit -m "feat(auth): add login form validation"
```

### 5. 完了画面

コミット成功時：
```
✅ コミット完了：feat(auth): add login form validation (abc1234)

次のステップ：
  - git push で リモートにプッシュ
  - /create-pull-request で PR を作成
```

## コミットタイプの選び方

| Type | 用途 |
|------|------|
| `feat` | 新しい機能やを追加したとき |
| `fix` | バグを修正したとき |
| `docs` | ドキュメント（.md など）のみ変更したとき |
| `style` | コード形式を整えたとき（非機能） |
| `refactor` | コードを再構成したとき（動作変わらず） |
| `perf` | パフォーマンスを改善したとき |
| `test` | テストを追加・修正したとき |
| `chore` | 依存関係やビルド設定を変更したとき |

## メッセージ作成ルール

### 命令形で書く
- ✅ 良い例：`Add`, `Fix`, `Update`
- ❌ 悪い例：`Added`, `Fixed`, `Adding`

### 具体的に書く
- ✅ 良い例：`Fix validation error in email field`
- ❌ 悪い例：`Fix bug`

### 簡潔に書く
- 最大50文字以下
- 要点を絞る

### ピリオドなし
- ✅ 良い例：`add login form validation`
- ❌ 悪い例：`add login form validation.`

### 最初の文字は大文字
- ✅ 良い例：`Add login form validation`
- ❌ 悪い例：`add login form validation`

## Scope の付け方

Scope は変更の影響を受けるエリアを示します（オプション）

### 書き方
- 小文字で記述：`auth`, `api`, `ui`
- 複合語はハイフンで接続：`auth-service`, `api-v1`
- 1～3単語程度に抑える

### 例
```
feat(auth): add password reset
fix(api): resolve timeout issue
docs(readme): update installation steps
refactor(ui-components): simplify button component
```

## 使用例

### パターンA：高速フロー（メッセージを直接入力）

```
user: /git-commit feat(auth): add login form validation

✅ ステージされたファイル：
   - src/pages/login.tsx
   - src/components/LoginForm.tsx

✅ フォーマット検証完了：feat(auth): add login form validation

実行してもよろしいですか？ [y/n]
user: y

✅ コミット完了：feat(auth): add login form validation (abc1234)

次のステップ：git push でリモートにプッシュできます
```

**所要時間：数秒**

### パターンB：対話的フロー（ガイド付き）

```
user: /git-commit

✅ ステージされたファイル：
   - src/pages/login.tsx
   - src/components/LoginForm.tsx

Copilot: コミットタイプを選択してください：
  feat      - 新しい機能を追加
  fix       - バグを修正
  ...

user: feat

Copilot: 影響を受ける領域/コンポーネント？[Enterで省略]

user: auth

Copilot: 簡潔な説明を命令形で入力してください（最大50文字）：

user: add login form validation

✅ フォーマット検証完了

以下でコミットします：

feat(auth): add login form validation

実行してもよろしいですか？ [y/n]

user: y

✅ コミット完了：feat(auth): add login form validation (abc1234)

次のステップ：git push でリモートにプッシュできます
```

**所要時間：30秒～1分**

### パターンA：フォーマットエラーの場合

```
user: /git-commit feat(auth): add new login form validation with several new features

✅ ステージされたファイル：
   - src/pages/login.tsx
   - src/components/LoginForm.tsx

❌ 検証エラー：
  - Description が70文字です（最大50文字）

修正して再度実行してください：
user: /git-commit feat(auth): add login form validation

✅ フォーマット検証完了：feat(auth): add login form validation

実行してもよろしいですか？ [y/n]

user: y

✅ コミット完了：feat(auth): add login form validation (abc1234)
```
