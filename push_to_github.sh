#!/bin/bash
echo ""
echo "=== CalciTrack GitHub Push ==="
echo "Enter your GitHub Personal Access Token (it will not be visible):"
read -s TOKEN
echo ""

echo "Setting git author..."
printf '[user]\n\tname = Sai Keerthana Cherukuri\n\temail = saikeerthana999@github.com\n' > ~/.gitconfig

printf "https://saikeerthana999:${TOKEN}@github.com\n" > ~/.git-credentials

REMOTE="https://saikeerthana999:${TOKEN}@github.com/saikeerthana999/CalciTrack.git"

echo "Removing Replit-specific files from index..."
git rm --cached --ignore-unmatch .replit replit.md uv.lock main.py .streamlit/config.toml 2>/dev/null
git add -A 2>/dev/null

echo "Fetching current GitHub state..."
git fetch origin 2>/dev/null
PARENT=$(git rev-parse origin/main 2>/dev/null)

echo "Creating clean commit..."
TREE=$(git write-tree)
DATE=$(date -u "+%Y-%m-%d %H:%M UTC")

export GIT_AUTHOR_NAME="Sai Keerthana Cherukuri"
export GIT_AUTHOR_EMAIL="saikeerthana999@github.com"
export GIT_COMMITTER_NAME="Sai Keerthana Cherukuri"
export GIT_COMMITTER_EMAIL="saikeerthana999@github.com"

if [ -n "$PARENT" ]; then
    NEW_COMMIT=$(git commit-tree "$TREE" -p "$PARENT" -m "CalciTrack — ${DATE}")
    git push "$REMOTE" "${NEW_COMMIT}:refs/heads/main"
else
    NEW_COMMIT=$(git commit-tree "$TREE" -m "CalciTrack — initial commit")
    git push "$REMOTE" "${NEW_COMMIT}:refs/heads/main" --force
fi

echo ""
echo "Done! Visit: https://github.com/saikeerthana999/CalciTrack"
