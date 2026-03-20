#!/bin/bash
echo ""
echo "=== CalciTrack GitHub Push ==="
echo "Enter your GitHub Personal Access Token (it will not be visible):"
read -s TOKEN
echo ""
echo "Setting credentials..."
echo "https://saikeerthana999:${TOKEN}@github.com" > ~/.git-credentials
git config credential.helper store
echo "Pushing to saikeerthana999/CalciTrack..."
git push -u origin main
echo ""
echo "Done!"
