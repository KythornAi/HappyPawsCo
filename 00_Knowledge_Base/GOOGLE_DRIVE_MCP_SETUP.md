# Google Drive MCP Setup Guide

**Date**: January 11, 2026
**Status**: ✅ MCP Installed and Connected

---

## ✅ Installation Complete

The Google Drive/Sheets MCP server has been successfully installed:

```bash
MCP Name: google-drive
Package: @isaacphi/mcp-gdrive
Status: ✓ Connected
Scope: Local (private to this project)
```

---

## 🔐 Authentication Setup Required

The MCP is installed but needs Google Cloud OAuth credentials to access your Google Drive and Sheets.

### Step 1: Locate Your Existing Google Cloud Credentials

Since you already set up Google Cloud OAuth for Make.com, you should have:
- **OAuth Client ID** (looks like: `xxxxx.apps.googleusercontent.com`)
- **OAuth Client Secret**
- **Credentials JSON file** (downloaded from Google Cloud Console)

Look for these in your Make.com setup documentation or Google Cloud Console.

### Step 2: Set Environment Variables

You need to configure these environment variables for the MCP:

```bash
export GDRIVE_CREDS_DIR="/path/to/credentials/folder"
export CLIENT_ID="your-client-id.apps.googleusercontent.com"
export CLIENT_SECRET="your-client-secret"
```

**Option A: Add to your shell profile** (persistent across sessions)
```bash
# Add to ~/.zshrc or ~/.bash_profile
echo 'export GDRIVE_CREDS_DIR="$HOME/.config/google-drive-mcp"' >> ~/.zshrc
echo 'export CLIENT_ID="your-actual-client-id"' >> ~/.zshrc
echo 'export CLIENT_SECRET="your-actual-client-secret"' >> ~/.zshrc
source ~/.zshrc
```

**Option B: Add to Claude Code MCP config** (recommended)
```bash
# Add environment variables when configuring the MCP
claude mcp remove google-drive
claude mcp add --transport stdio google-drive \
  --env GDRIVE_CREDS_DIR="$HOME/.config/google-drive-mcp" \
  --env CLIENT_ID="your-client-id" \
  --env CLIENT_SECRET="your-client-secret" \
  -- npx -y @isaacphi/mcp-gdrive
```

### Step 3: Create Credentials Directory

```bash
mkdir -p ~/.config/google-drive-mcp
```

### Step 4: Add OAuth Credentials File

If you have the credentials JSON file from Google Cloud:
```bash
cp /path/to/your/gcp-oauth.keys.json ~/.config/google-drive-mcp/
```

---

## 🔑 If You Don't Have Google Cloud OAuth Yet

### Create New OAuth Credentials

1. **Go to Google Cloud Console**: https://console.cloud.google.com

2. **Create/Select Project**:
   - Create new project: "HappyPawsCo Claude Integration"
   - OR use existing Make.com project

3. **Enable Required APIs**:
   - Google Drive API
   - Google Sheets API
   - Google Docs API

4. **Configure OAuth Consent Screen**:
   - User Type: Internal (for testing) or External
   - App name: HappyPawsCo Claude
   - Add your email as test user

5. **Create OAuth Client ID**:
   - Credentials → Create Credentials → OAuth Client ID
   - Application type: **Desktop app**
   - Name: Claude Code MCP
   - Download JSON file

6. **Save Credentials**:
   ```bash
   mv ~/Downloads/client_secret_*.json ~/.config/google-drive-mcp/gcp-oauth.keys.json
   ```

---

## 🧪 Test Authentication

Once credentials are configured, test the MCP by trying to list Google Sheets:

Ask me:
```
List all Google Sheets in my Drive
```

Or:
```
Search for files named "product" in my Google Drive
```

The first time, it will open a browser for OAuth authentication. After that, tokens are saved and authentication is automatic.

---

## 🛠️ Available Tools

Once authenticated, you can use:

| Tool | Description | Example Use |
|------|-------------|-------------|
| `gdrive_search` | Find files by query | "Find all spreadsheets with 'product' in the name" |
| `gdrive_read_file` | Read file contents | "Read the contents of [file-id]" |
| `gsheets_read` | Read spreadsheet data | "Read rows 1-10 from Sheet1 in [spreadsheet-id]" |
| `gsheets_update_cell` | Update cell values | "Update cell A1 to 'Updated' in [spreadsheet-id]" |

---

## 📊 Use Cases for HappyPawsCo

### Product Database Access
```
Read all products from the HappyPawsCo product database spreadsheet
```

### Research Document Access
```
Find and read the latest research brief in Google Drive
```

### Blog Tracking
```
Update the blog tracking sheet with today's published blog
```

### Brand Assets Search
```
Search for logo files in the brand assets folder
```

---

## 🔧 Troubleshooting

### MCP shows "Not Connected"
```bash
# Restart Claude Code or reconnect MCP
claude mcp list
```

### Authentication fails
- Verify CLIENT_ID and CLIENT_SECRET are correct
- Check that APIs are enabled in Google Cloud Console
- Ensure you're added as a test user in OAuth consent screen

### Can't find credentials
- Check Make.com integration settings for Google Cloud credentials
- Look in Google Cloud Console → Credentials
- Download new OAuth Client ID if needed

---

## 📝 Next Steps

1. **Locate or create Google Cloud OAuth credentials**
2. **Set environment variables** (use Option B above for best results)
3. **Test authentication** by asking me to list your Google Sheets
4. **Once working**: I can create agents that automatically access your product database

---

**Current Status**: MCP installed ✅ | Authentication pending ⏳
