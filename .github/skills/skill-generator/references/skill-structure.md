# スキル構造ガイド

## ディレクトリレイアウト

```
.github/skills/<name>/
├── SKILL.md              必須：スキルのメタデータと説明
├── README.md             推奨：詳細な使用ガイド
├── references/           オプション：参考資料
│   ├── architecture.md
│   └── reference-*.md
└── assets/               オプション：テンプレートやスクリプト
    ├── templates/
    └── scripts/
```

## 各ファイルの役割

### SKILL.md（必須）
- スキルの宣言ファイル
- YAML frontmatter でメタデータ定義
- 簡潔な説明と使用場面
- リソース参照

### README.md（推奨）
- クイックスタート手順
- 詳細な処理フロー
- トラブルシューティング

### references/
- 参考資料（複数ファイル可）
- SKILL.md から参照
- 1 レベル深いパスで参照

### assets/
- テンプレートファイル
- 実行スクリプト
- 設定ファイル雛形

## ファイルサイズ目安

- SKILL.md: 500 行以内
- README.md: 300 行以内
- リファレンス: 各 200 行以内
