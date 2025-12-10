#!/bin/sh
set -e  # Exit immediately if any command fails

echo "=== Starting DoggyDex container ==="

echo "Step 1: Decoding service account and generating dogs.json"
# If SERVICE_ACCOUNT_JSON_B64 is set, decode it to a file
if [ -n "$SERVICE_ACCOUNT_JSON_B64" ]; then
  echo "$SERVICE_ACCOUNT_JSON_B64" | base64 --decode > .secrets/service_account.json
fi

# Run the script to generate dogs.json
python googletojson.py

echo "Step 2: Starting API"
# Run your API
exec python main.py


