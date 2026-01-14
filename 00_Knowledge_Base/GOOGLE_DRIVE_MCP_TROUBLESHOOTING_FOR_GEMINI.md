# Google Drive MCP Authentication Troubleshooting - Help Needed

**Date**: January 11, 2026
**Context**: Setting up Google Drive/Sheets MCP for Claude Code CLI
**Problem**: Cannot complete OAuth authentication - getting 403 "unregistered callers" error

---

## 🎯 GOAL

Set up Google Drive MCP server for Claude Code so I can:
- Read Google Sheets (product database)
- Search Google Drive files
- Access research documents
- Update spreadsheet cells

---

## 🔧 ENVIRONMENT

**System**: macOS (Darwin 25.1.0)
**Claude Code Version**: 2.1.4
**Working Directory**: `/Volumes/Home Ext/Home Ext/Desktop/Claude`

**Current MCPs** (working fine):
- github ✅
- filesystem ✅
- everything ✅
- thinking ✅

---

## 📋 WHAT WE'VE TRIED (In Order)

### Attempt 1: @isaacphi/mcp-gdrive
**Installation**:
```bash
claude mcp add --transport stdio google-drive -- npx -y @isaacphi/mcp-gdrive
```

**Configuration**:
- Google Cloud Project: "MCP Google Drive"
- APIs Enabled: Drive API, Sheets API, Docs API
- OAuth Consent Screen: Configured with scopes:
  - `https://www.googleapis.com/auth/drive`
  - `https://www.googleapis.com/auth/spreadsheets`
  - `https://www.googleapis.com/auth/documents`

**Credentials Tried**:
1. Desktop App OAuth (first attempt)
2. Web Application OAuth (second attempt - got redirect_uri_mismatch)
3. Back to Desktop App OAuth (current)

**Current Configuration**:
```
GDRIVE_CREDS_DIR=/Volumes/Home Ext/Home Ext/.config/google-drive-mcp
CLIENT_ID=[REDACTED - see local config]
CLIENT_SECRET=[REDACTED - see local config]
```

**File Created**: `~/.config/google-drive-mcp/gcp-oauth.keys.json`
```json
{
  "installed": {
    "client_id": "[REDACTED]",
    "project_id": "mcp-google-drive",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_secret": "[REDACTED]",
    "redirect_uris": ["urn:ietf:wg:oauth:2.0:oob", "http://localhost"]
  }
}
```

**Result**: 
- MCP shows as "Connected" in `claude mcp list`
- But when trying to use: `MCP error 403: Method doesn't allow unregistered callers`
- Browser NEVER opens for OAuth authentication
- Tried running `npx -y @isaacphi/mcp-gdrive` directly - no browser opens

### Attempt 2: @modelcontextprotocol/server-gdrive (Official)
**Command Tried**:
```bash
npx -y @modelcontextprotocol/server-gdrive auth
```

**Result**: Command ran but browser didn't open, process ended quickly

---

## ❌ ERRORS ENCOUNTERED

### Primary Error:
```
MCP error 403: Method doesn't allow unregistered callers (callers without established identity). 
Please use API Key or other form of API consumer identity to call this API.
```

### Secondary Error (when tried Web app OAuth):
```
Error 400: redirect_uri_mismatch
```

### Observations:
- MCP server shows as "Connected" in health check
- OAuth browser flow NEVER triggers (even when running MCP directly)
- Only time browser opens is when OAuth is blocked/rejected
- No token file ever gets created (should create something like `.gdrive-server-credentials.json`)

---

## ✅ WHAT IS WORKING

1. **Google Cloud Project Setup**:
   - Project created successfully
   - All 3 APIs enabled (Drive, Sheets, Docs)
   - OAuth consent screen fully configured
   - Desktop app OAuth credentials generated
   - Test user added (user's email)

2. **Claude Code MCP Configuration**:
   - MCP added successfully
   - Shows as "Connected" in health check
   - Environment variables properly set
   - Config file exists and is valid JSON

3. **Other MCPs**:
   - All 4 other MCP servers work perfectly
   - No authentication issues with them

---

## 🤔 THEORIES ON WHAT'S WRONG

1. **OAuth Flow Not Triggering**: The MCP servers we've tried aren't successfully opening a browser for authentication
   - Possible cause: Node.js environment issue?
   - Possible cause: MCP server doesn't support this auth method?

2. **Google Cloud Configuration Issue**: Something in the OAuth setup prevents authentication
   - Possible cause: "Testing" status expires tokens after 7 days (mentioned in documentation)
   - Possible cause: Need to publish app instead of keeping in testing?
   - Possible cause: Missing some OAuth configuration?

3. **MCP Server Compatibility**: These MCP servers might not work properly with Claude Code CLI
   - Official docs mention OAuth 2.0 support via `/mcp` command
   - But we're using CLI, not desktop app

---

## 📚 DOCUMENTATION REFERENCES

**MCP Servers Tried**:
1. [@isaacphi/mcp-gdrive](https://github.com/isaacphi/mcp-gdrive)
2. [@modelcontextprotocol/server-gdrive](https://www.npmjs.com/package/@modelcontextprotocol/server-gdrive)

**Alternative Servers Found** (not yet tried):
- [@piotr-agier/google-drive-mcp](https://github.com/piotr-agier/google-drive-mcp) - Has explicit `auth` command
- [google-workspace-mcp-with-script](https://github.com/sputnicyoji/google-workspace-mcp-with-script) - Full Workspace integration

---

## 🎯 QUESTIONS FOR GEMINI

1. **Why isn't the OAuth browser flow triggering?**
   - Is there a Node.js/npm configuration issue?
   - Do these MCP servers require a specific setup?

2. **Should we use a different MCP server?**
   - Which Google Drive MCP server is most reliable for Claude Code CLI?
   - Is there one that definitely works with macOS authentication?

3. **Google Cloud OAuth Setup**:
   - Do we need to publish the OAuth app (move from "Testing" to "Production")?
   - Are there specific OAuth consent screen settings needed?
   - Should we use Web app instead of Desktop app?

4. **Authentication Method**:
   - Should we use Claude Code's `/mcp` command for OAuth?
   - Is there a manual way to generate and save OAuth tokens?
   - Can we use service account credentials instead?

5. **Debugging Steps**:
   - How can we see detailed logs from the MCP server?
   - Is there a way to test OAuth authentication separately?
   - What's the correct redirect URI for Desktop apps in 2026?

---

## 🔍 SIMILAR WORKING SETUP

User has working Google OAuth for Make.com → Vertex AI (image generation)
- This proves the Google account CAN authenticate with Google Cloud
- Different OAuth client (don't want to interfere with that)
- But shows the account/organization setup is correct

---

## 💡 WHAT WOULD SUCCESS LOOK LIKE

1. Run command (or restart Claude Code)
2. Browser opens with Google sign-in
3. User authenticates and grants permissions
4. OAuth tokens saved locally
5. MCP can successfully call `gdrive_search` tool
6. Can list Google Sheets and read spreadsheet data

---

## 🚨 URGENT QUESTION

**Is there a simpler/better Google Drive MCP server we should be using instead?**

We've spent hours on OAuth authentication when the actual goal is just to read Google Sheets data. Maybe we're using the wrong approach entirely?

---

**Next Steps After Gemini Input**: Will try recommended solution and report back results.
