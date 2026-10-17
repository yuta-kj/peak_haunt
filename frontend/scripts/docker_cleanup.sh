#!/bin/bash
echo "🧹 Docker cleanup 開始..."

# dangling イメージ・コンテナを削除
docker system prune -f

# 古いキャッシュを削除（オプション）
docker builder prune -f

echo "✅ cleanup 完了"
docker system df
