# WordPress MCP Server

Connect AI assistants (Claude Code, Cursor) to WordPress sites via the REST API.

## Installation

```bash
cd wordpress-mcp
uv sync
```

## Configuration

Set environment variables:

```bash
export WORDPRESS_URL=https://your-site.com
export WORDPRESS_USER=admin
export WORDPRESS_APP_PASSWORD=xxxx-xxxx-xxxx-xxxx
```

### Getting an Application Password

1. Go to WordPress Admin > Users > Profile
2. Scroll to "Application Passwords"
3. Enter a name (e.g., "Claude Code") and click "Add New"
4. Copy the generated password

## Usage with Claude Code

Add to `~/.claude/config.json`:

```json
{
  "mcpServers": {
    "wordpress": {
      "command": "uv",
      "args": ["run", "--directory", "/path/to/wordpress-mcp", "wordpress-mcp"],
      "env": {
        "WORDPRESS_URL": "https://your-site.com",
        "WORDPRESS_USER": "admin",
        "WORDPRESS_APP_PASSWORD": "xxxx-xxxx-xxxx-xxxx"
      }
    }
  }
}
```

## Available Tools

| Tool | Description | Auth Required |
|------|-------------|---------------|
| `wp_get_posts` | List posts with filtering | No (for published) |
| `wp_get_pages` | List pages | No |
| `wp_get_media` | List media library items | No |
| `wp_get_plugins` | List installed plugins | Yes |
| `wp_site_info` | Get site information | No |

## Examples

Once configured, you can ask Claude:

- "Show me the latest 5 posts on my WordPress site"
- "What plugins are installed?"
- "Search for posts about 'security'"
- "Get site information"
