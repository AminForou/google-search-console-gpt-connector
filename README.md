# Google Search Console MCP Server

This is a MCP (Machine Callable Program) server for interacting with Google Search Console API.

## Setup

1. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a Google Cloud service account and download credentials:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select an existing one
   - Enable the Search Console API for your project
   - Go to "IAM & Admin" > "Service Accounts"
   - Create a new service account
   - Grant it the necessary permissions (at least "Search Console API > Search Console API User" role)
   - Create a JSON key for this service account
   - Download the key and save it as `service_account_credentials.json` in this directory

4. Add your Search Console property to the service account:
   - In Google Search Console, add the service account email as a user to your property

## Usage

Run the server:

```
python -m mcp_gsc.main
```

<<<<<<< HEAD
The server provides the following tools:
- `list_properties`: Lists all Search Console properties accessible to the service account 

## ChatGPT Connector Compatibility

This MCP implements the standard `search` and `fetch` surfaces required by [OpenAI's connector specification](https://platform.openai.com/docs/assistants/tools/mcp#connectors). The `search` tool returns enriched metadata (title, snippet, URL, timestamp, score, and connector-specific payload) so that ChatGPT can present actionable cards for properties, sitemap files, URL inspections, and Search Analytics snapshots. The `fetch` tool resolves the opaque `id` values returned by `search` into full Markdown documents along with a `mimeType` and structured metadata that the connector runtime caches.

When you register the server as a connector within ChatGPT, ensure that:
1. The MCP server is reachable from the connector runtime (usually via `mcp-gsc` script or `python mcp-gsc/gsc_server.py`).
2. Required Google Search Console credentials are configured through environment variables or the local credential files described above.
3. The connector manifest references the `search` and `fetch` tool names exposed by this server.

This setup lets ChatGPT issue autonomous queries (e.g., "top queries last 14 days" or "check sitemap errors") and fetch the supporting detail on demand without manual prompt engineering.
=======
The server exposes several MCP tools, including:

- `list_properties`: List Search Console properties accessible to the configured credentials.
- `delete_site`: Remove a Search Console property from the authenticated account.
- `get_search_analytics`: Retrieve performance metrics with configurable dimensions and lookback windows.
- `get_site_details`: Display metadata and verification status for a property.
- `get_sitemaps`: Summarize submitted sitemaps and their statuses.
- `inspect_url_enhanced`: Run the Search Console URL Inspection API for a specific page.
- `batch_url_inspection`: Inspect up to 10 URLs at once for quick diagnostics.
- `manage_sitemaps`: Submit, remove, or review sitemap information.
- `connector_search`: Search entry point required by ChatGPT connectors.
- `connector_fetch`: Fetch entry point required by ChatGPT connectors.
- `get_creator_info`: Basic information about the tool author.
>>>>>>> 51e85885d9f5b4d5e05b7c0a531a0f5cb7112f5e
