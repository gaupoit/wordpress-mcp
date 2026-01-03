"""Configuration management for WordPress MCP Server."""

import os
from dataclasses import dataclass


@dataclass
class Config:
    """WordPress connection configuration."""

    url: str
    user: str | None = None
    app_password: str | None = None

    @property
    def has_auth(self) -> bool:
        """Check if authentication credentials are available."""
        return bool(self.user and self.app_password)

    @property
    def api_base(self) -> str:
        """Get the REST API base URL."""
        base = self.url.rstrip("/")
        return f"{base}/wp-json/wp/v2"


def load_config() -> Config:
    """Load configuration from environment variables."""
    url = os.environ.get("WORDPRESS_URL", "")
    if not url:
        raise ValueError("WORDPRESS_URL environment variable is required")

    return Config(
        url=url,
        user=os.environ.get("WORDPRESS_USER"),
        app_password=os.environ.get("WORDPRESS_APP_PASSWORD"),
    )
