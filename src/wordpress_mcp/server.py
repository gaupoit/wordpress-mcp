"""WordPress MCP Server - Connect AI assistants to WordPress sites."""

from mcp.server.fastmcp import FastMCP

from .client import WordPressClient
from .config import load_config

# Initialize the MCP server
mcp = FastMCP("WordPress")

# Global client instance (initialized on first use)
_client: WordPressClient | None = None


def get_client() -> WordPressClient:
    """Get or create the WordPress client."""
    global _client
    if _client is None:
        config = load_config()
        _client = WordPressClient(config)
    return _client


@mcp.tool()
def wp_get_posts(
    status: str = "publish",
    per_page: int = 10,
    search: str | None = None,
) -> list[dict]:
    """Get posts from WordPress.

    Args:
        status: Post status filter - 'publish', 'draft', or 'all'. Default is 'publish'.
        per_page: Number of posts to return (1-100). Default is 10.
        search: Search term to filter posts by title/content.

    Returns:
        List of posts with id, title, status, date, slug, excerpt, and link.
    """
    client = get_client()
    return client.get_posts(status=status, per_page=per_page, search=search)


@mcp.tool()
def wp_get_pages(
    per_page: int = 10,
    search: str | None = None,
) -> list[dict]:
    """Get pages from WordPress.

    Args:
        per_page: Number of pages to return (1-100). Default is 10.
        search: Search term to filter pages by title/content.

    Returns:
        List of pages with id, title, status, slug, and link.
    """
    client = get_client()
    return client.get_pages(per_page=per_page, search=search)


@mcp.tool()
def wp_get_media(
    per_page: int = 10,
    media_type: str | None = None,
) -> list[dict]:
    """Get media items from WordPress media library.

    Args:
        per_page: Number of items to return (1-100). Default is 10.
        media_type: Filter by type - 'image', 'video', 'audio', or 'application'.

    Returns:
        List of media items with id, title, url, mime_type, and alt_text.
    """
    client = get_client()
    return client.get_media(per_page=per_page, media_type=media_type)


@mcp.tool()
def wp_get_plugins(status: str = "all") -> list[dict]:
    """Get installed plugins from WordPress. Requires authentication.

    Args:
        status: Filter by status - 'active', 'inactive', or 'all'. Default is 'all'.

    Returns:
        List of plugins with name, plugin slug, status, version, and description.
    """
    client = get_client()
    return client.get_plugins(status=status)


@mcp.tool()
def wp_site_info() -> dict:
    """Get WordPress site information.

    Returns:
        Site info including name, description, url, home, gmt_offset, and timezone.
    """
    client = get_client()
    return client.get_site_info()


@mcp.tool()
def wp_get_post(post_id: int) -> dict:
    """Get a single post by ID with full content.

    Args:
        post_id: The ID of the post to retrieve.

    Returns:
        Post with id, title, content (raw), excerpt, status, date, slug, and link.
    """
    client = get_client()
    return client.get_post(post_id)


@mcp.tool()
def wp_create_post(
    title: str,
    content: str,
    status: str = "draft",
    excerpt: str | None = None,
) -> dict:
    """Create a new WordPress post.

    Args:
        title: The title of the post.
        content: The content/body of the post (supports HTML and Gutenberg blocks).
        status: Post status - 'draft', 'publish', 'pending', 'private'. Default is 'draft'.
        excerpt: Optional excerpt/summary of the post.

    Returns:
        Created post with id, title, status, date, and link.
    """
    client = get_client()
    return client.create_post(title=title, content=content, status=status, excerpt=excerpt)


@mcp.tool()
def wp_update_post(
    post_id: int,
    title: str | None = None,
    content: str | None = None,
    status: str | None = None,
    excerpt: str | None = None,
) -> dict:
    """Update an existing WordPress post.

    Args:
        post_id: The ID of the post to update.
        title: New title (optional).
        content: New content (optional).
        status: New status - 'draft', 'publish', 'pending', 'private', 'trash' (optional).
        excerpt: New excerpt (optional).

    Returns:
        Updated post with id, title, status, date, and link.
    """
    client = get_client()
    return client.update_post(
        post_id=post_id, title=title, content=content, status=status, excerpt=excerpt
    )


@mcp.tool()
def wp_delete_post(post_id: int, force: bool = False) -> dict:
    """Delete a WordPress post.

    Args:
        post_id: The ID of the post to delete.
        force: If False (default), moves to trash. If True, permanently deletes.

    Returns:
        Confirmation with id, deleted status, and previous post info.
    """
    client = get_client()
    return client.delete_post(post_id=post_id, force=force)


def main():
    """Entry point for the WordPress MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
