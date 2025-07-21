#!/bin/bash

echo "Starting deployment..."

# Pull the latest code
git pull origin main

# Build and start the Docker containers
docker-compose up -d --build

echo "Deployment finished!"
