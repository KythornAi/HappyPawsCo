# MCP Server Installation Options

**Date**: January 11, 2026
**Purpose**: Available MCP servers for HappyPawsCo automation

---

## ✅ Currently Installed (4 MCPs)

1. **github** - GitHub repository management
2. **filesystem** - File operations
3. **everything** - Testing/demonstration
4. **thinking** - Sequential thinking

---

## 🔍 Recommended MCPs for Installation

### 1. Google Drive/Sheets MCP

**Best Option: `@isaacphi/mcp-gdrive`**

**Purpose**:
- Access product databases in Google Sheets
- Read research documents from Google Drive
- Update spreadsheets with blog data
- Search for files across Drive

**Installation Command**:
```bash
claude mcp add --transport stdio google-drive -- npx -y @isaacphi/mcp-gdrive
```

**Authentication Required**:
1. Create Google Cloud project
2. Enable Google Drive API, Sheets API, Docs API
3. Configure OAuth consent screen
4. Generate OAuth Client ID (Desktop App)
5. Download credentials as `gcp-oauth.keys.json`
6. Set environment variables:
   - `GDRIVE_CREDS_DIR`: Path to credentials directory
   - `CLIENT_ID`: Your OAuth Client ID
   - `CLIENT_SECRET`: Your OAuth Client Secret

**Available Tools**:
- `gdrive_search` - Find files by query
- `gdrive_read_file` - Read file contents
- `gsheets_read` - Read spreadsheet data
- `gsheets_update_cell` - Update cells

**Use Cases for HappyPawsCo**:
- Read product database from Google Sheets
- Access research brief documents
- Update blog tracking spreadsheet
- Search for brand assets

**GitHub**: [isaacphi/mcp-gdrive](https://github.com/isaacphi/mcp-gdrive)

---

### 2. Shopify MCP

**Available Option: `shopify-mcp-server` by siddhantbajaj**

**Purpose**:
- Retrieve product lists from Shopify store
- Access customer data
- Future: Auto-publish blogs to Shopify

**Installation** (Python-based):
```bash
git clone https://github.com/siddhantbajaj/shopify-mcp-server.git
cd shopify-mcp-server
uv venv
source .venv/bin/activate
uv pip install -e .
```

**Authentication Required**:
Create `.env` file with:
- `SHOPIFY_SHOP_URL` - your-store.myshopify.com
- `SHOPIFY_API_KEY` - API key
- `SHOPIFY_PASSWORD` - API password
- `SHOPIFY_ACCESS_TOKEN` - Access token

**Available Tools** (Current):
- `get-product-list` - Retrieve products from store
- `get-customer-list` - Retrieve customer list

**Limitations**:
- Only 2 tools currently (products + customers)
- No blog publishing capability yet
- Python-based (not NPM)

**Use Cases for HappyPawsCo**:
- Verify product availability for blog links
- Check product details for accurate descriptions
- Future: Auto-publish polished blogs

**GitHub**: [siddhantbajaj/shopify-mcp-server](https://github.com/siddhantbajaj/shopify-mcp-server)

**⚠️ Note**: This is community-built and has limited features. May want to wait for official Shopify MCP or build custom.

---

## 🎯 Recommendation

### Install Now:
✅ **Google Drive/Sheets MCP** - High value, widely useful
  - Access product database
  - Read research documents
  - Update tracking sheets
  - Well-maintained, active development

### Consider Later:
⏸️ **Shopify MCP** - Limited features currently
  - Only has product/customer listing (no publish capability)
  - Python-based (different from your current NPM setup)
  - May want to build custom Shopify integration when ready for auto-publishing

---

## Installation Process (Google Drive MCP)

### Step 1: Install the MCP Server
```bash
claude mcp add --transport stdio google-drive -- npx -y @isaacphi/mcp-gdrive
```

### Step 2: Set Up Google Cloud Project
1. Go to https://console.cloud.google.com
2. Create new project (name: "HappyPawsCo Claude Integration")
3. Enable APIs:
   - Google Drive API
   - Google Sheets API
   - Google Docs API
4. Create OAuth Client ID (Desktop app type)
5. Download credentials

### Step 3: Configure Authentication
```bash
# Set environment variables
export GDRIVE_CREDS_DIR="/path/to/credentials"
export CLIENT_ID="your-client-id.apps.googleusercontent.com"
export CLIENT_SECRET="your-client-secret"
```

### Step 4: Authenticate
The first time you use the MCP, it will open a browser for OAuth authentication. After authentication, tokens are saved for future use.

---

## Alternative Google MCP Servers

If `@isaacphi/mcp-gdrive` doesn't meet needs, alternatives include:

1. **piotr-agier/google-drive-mcp** - More comprehensive Drive integration
2. **shionhonda/mcp-gsheet** - Google Sheets only (simpler setup)
3. **distrihub/mcp-google-workspace** - Rust-based (faster performance)

---

## Sources

- [MCP Google Drive Server](https://github.com/isaacphi/mcp-gdrive)
- [Shopify MCP Server](https://github.com/siddhantbajaj/shopify-mcp-server)
- [MCP Official Servers Registry](https://github.com/modelcontextprotocol/servers)
- [Claude Code MCP Documentation](https://code.claude.com/docs/en/mcp)
