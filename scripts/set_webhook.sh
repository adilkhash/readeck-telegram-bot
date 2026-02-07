#!/usr/bin/env bash
set -euo pipefail

if [ $# -ne 2 ]; then
  echo "Usage: $0 <TELEGRAM_BOT_TOKEN> <LAMBDA_FUNCTION_URL>"
  exit 1
fi

TOKEN="$1"
LAMBDA_URL="$2"

curl -s "https://api.telegram.org/bot${TOKEN}/setWebhook" \
  -d "url=${LAMBDA_URL}" | python3 -m json.tool
