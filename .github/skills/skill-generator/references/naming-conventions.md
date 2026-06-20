# スキル命名規則

## スキル名 (folder + name field)

形式: lowercase-with-hyphens

要件:
- 小文字のみ (a-z, 0-9, -)
- ハイフンで単語区切り
- 1-64 文字
- わかりやすく具体的

### 例

Good:
- git-commit
- project-setup-typescript
- database-migration
- code-review-automation

Bad:
- gitcommit (わかりにくい)
- git_commit (アンダースコア使用)
- GIT-COMMIT (大文字)
- do-stuff (曖昧)

## ファイル名

- スネークケース: api-reference.md
- わかりやすい説明名: architecture.md, setup-guide.md
- テンプレート: *-template.* または *-example.*

## フォルダ名

固定:
- references/ - 参考資料
- assets/ - テンプレートやスクリプト
- assets/templates/ - テンプレートファイル
- assets/scripts/ - 実行スクリプト

## メタデータ命名

frontmatter フィールド:
```yaml
---
name: skill-name          folder 名と一致
description: '...'        Use when: トリガー語を含める
argument-hint: '...'      オプション
user-invocable: true      デフォルト true
---
```
