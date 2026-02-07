#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

echo "Cleaning previous build..."
rm -rf packages package.zip

echo "Exporting dependencies..."
uv export --frozen --no-dev --no-editable > requirements.txt

echo "Installing dependencies to packages/..."
uv pip install \
  --target packages \
  --python-platform x86_64-manylinux_2_17 \
  --python-version 3.14 \
  -r requirements.txt

rm requirements.txt

echo "Creating package.zip..."
cd packages
zip -r ../package.zip . -q
cd ..
zip -r package.zip app/ -q

echo "Done! package.zip is ready for Lambda deployment."
