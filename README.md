# WordPress MCP Server

> Manage your WordPress site with AI. Create posts, update content, and query your site—all through natural conversation.

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![MCP](https://img.shields.io/badge/MCP-compatible-green.svg)](https://modelcontextprotocol.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## What is this?

WordPress MCP is a [Model Context Protocol](https://modelcontextprotocol.io/) server that connects AI assistants like **Claude Code** and **Cursor** to your WordPress site via the REST API.

Instead of switching between your terminal and WordPress admin, just ask:

```
You: "Create a draft post about our new product launch"
You: "Show me all posts from last week"
You: "Update post 42 to published status"
You: "What plugins are installed on my site?"
```

## Features

- **Full CRUD for Posts** - Create, read, update, and delete posts
- **Content Management** - List pages, media, and plugins
- **Search & Filter** - Find posts by status, keyword, or date
- **Draft Workflow** - Create drafts, review, then publish
- **Secure Auth** - Uses WordPress Application Passwords

## Quick Start

### 1. Install

```bash
git clone https://github.com/gaupoit/wordpress-mcp.git
cd wordpress-mcp
uv sync
```

### 2. Create a WordPress Application Password

1. Go to **WordPress Admin → Users → Profile**
2. Scroll to **Application Passwords**
3. Enter a name (e.g., "Claude Code") and click **Add New**
4. Copy the generated password (you won't see it again!)

### 3. Configure Claude Code

Add to your Claude Code MCP config (`~/.claude.json`):

```json
{
  "mcpServers": {
    "wordpress": {
      "command": "uv",
      "args": ["run", "--directory", "/path/to/wordpress-mcp", "wordpress-mcp"],
      "env": {
        "WORDPRESS_URL": "https://your-site.com",
        "WORDPRESS_USER": "your-username",
        "WORDPRESS_APP_PASSWORD": "xxxx-xxxx-xxxx-xxxx"
      }
    }
  }
}
```

### 4. Restart Claude Code

```bash
# Quit and restart
claude
```

Verify with `/mcp` - you should see "wordpress" listed.

## Available Tools

### Reading Content

| Tool | Description |
|------|-------------|
| `wp_site_info` | Get site name, URL, timezone |
| `wp_get_posts` | List posts (filter by status, search) |
| `wp_get_post` | Get single post with full content |
| `wp_get_pages` | List all pages |
| `wp_get_media` | List media library items |
| `wp_get_plugins` | List installed plugins |

### Writing Content

| Tool | Description |
|------|-------------|
| `wp_create_post` | Create a new post (draft or published) |
| `wp_update_post` | Update title, content, status, or excerpt |
| `wp_delete_post` | Move to trash or permanently delete |

## Example Workflows

### Blog Publishing

```
You: "Create a draft post titled 'Getting Started with AI' with an intro paragraph"
You: "Show me my draft posts"
You: "Update post 123 - add a conclusion section"
You: "Publish post 123"
```

### Content Audit

```
You: "List all draft posts"
You: "Search posts for 'outdated'"
You: "What plugins are currently active?"
```

### Bulk Operations

```
You: "Show me all posts with 'beta' in the title"
You: "Get the full content of post 45, 46, and 47"
You: "Move posts 45 and 46 to trash"
```

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `WORDPRESS_URL` | Yes | Your WordPress site URL (e.g., `https://example.com`) |
| `WORDPRESS_USER` | Yes | WordPress username |
| `WORDPRESS_APP_PASSWORD` | Yes | Application password (not your login password!) |

## Requirements

- Python 3.10+
- WordPress 5.6+ (for Application Passwords)
- WordPress REST API enabled (default on most sites)

## Troubleshooting

### "Authentication failed"
- Verify your Application Password is correct (no spaces)
- Ensure the user has permission to access REST API
- Check if a security plugin is blocking REST API

### "Connection refused"
- Verify `WORDPRESS_URL` includes `https://`
- Check if your site is behind a firewall/VPN

### Server not appearing in Claude Code
- Run `/mcp` to see error messages
- Test manually: `cd wordpress-mcp && uv run wordpress-mcp`
- Restart Claude Code completely (`/quit` then `claude`)

## Roadmap

- [ ] Categories and tags management
- [ ] User management
- [ ] Custom post types support
- [ ] Media upload
- [ ] Comments management
- [ ] WooCommerce integration

## Contributing

Contributions welcome! Please open an issue first to discuss what you'd like to change.

## License

MIT

---

Built with [FastMCP](https://github.com/jlowin/fastmcp) and the [WordPress REST API](https://developer.wordpress.org/rest-api/).
