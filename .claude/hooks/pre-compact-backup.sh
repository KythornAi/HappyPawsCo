#!/bin/bash

# Pre-Compaction Backup Script for HappyPawsCo
# This script runs BEFORE Claude compacts/summarizes the conversation
# It saves the full transcript so no details are lost

# Get the current date/time for filename
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")

# Define paths
PROJECT_DIR="/Volumes/Home Ext/Home Ext/Desktop/Claude"
BACKUP_DIR="$PROJECT_DIR/00_Session_Summary/compaction_backups"
BACKUP_FILE="$BACKUP_DIR/pre_compact_$TIMESTAMP.jsonl"

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Read the transcript path from stdin (passed by Claude Code)
# The hook receives JSON input with transcript_path
read -r INPUT
TRANSCRIPT_PATH=$(echo "$INPUT" | python3 -c "import sys, json; print(json.load(sys.stdin).get('transcript_path', ''))" 2>/dev/null)

# If we got a transcript path, copy it
if [ -n "$TRANSCRIPT_PATH" ] && [ -f "$TRANSCRIPT_PATH" ]; then
    cp "$TRANSCRIPT_PATH" "$BACKUP_FILE"
    echo "Transcript backed up to: $BACKUP_FILE" >> "$BACKUP_DIR/backup_log.txt"
    echo "$(date): Backed up $TRANSCRIPT_PATH" >> "$BACKUP_DIR/backup_log.txt"
else
    # Fallback: just log that compaction happened
    echo "$(date): PreCompact triggered but no transcript path found" >> "$BACKUP_DIR/backup_log.txt"
    echo "Input received: $INPUT" >> "$BACKUP_DIR/backup_log.txt"
fi

# Exit successfully so compaction can proceed
exit 0
