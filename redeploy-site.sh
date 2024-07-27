#!/bin/bash

# Navigate to the project directory
echo "Navigating to the project directory..."
cd /root/mlh-portfolio || { echo "Failed to navigate to project directory"; exit 1; }

# Fetch the latest changes from the main branch on GitHub
echo "Fetching the latest changes from the main branch..."
git fetch && git reset origin/main --hard || { echo "Failed to fetch and reset git repository"; exit 1; }

# Spin the containers down to prevent out of memor issues on our VPS instances
docker compose -f docker-compose.yml down

# Spin the container up
docker compose -f docker-compose.yml up -d --build

chmod +x /root/mlh-portfolio/redeploy-site.sh