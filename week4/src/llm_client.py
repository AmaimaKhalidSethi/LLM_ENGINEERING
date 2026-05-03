"""
llm_client.py
=============
Unified factory for OpenAI-compatible LLM clients.

All providers (Groq, OpenRouter, Gemini) expose an OpenAI-compatible REST
API, so we use a single ``openai.OpenAI`` instance per provider rather than
mixing different SDKs.

Important: ``reasoning_effort`` is an OpenAI-only parameter.
Groq and OpenRouter raise errors when it is included — do NOT pass it here.

Used by: day4.ipynb, day5.ipynb, python_to_go_generator.ipynb
"""

import os
from dotenv import load_dotenv
from openai import OpenAI


# Provider base URLs
GROQ_URL       = "https://api.groq.com/openai/v1"
OPENROUTER_URL = "https://openrouter.ai/api/v1"
GEMINI_URL     = "https://generativelanguage.googleapis.com/v1beta/openai/"


def build_clients(
    load_env: bool = True,
) -> dict[str, OpenAI | None]:
    """
    Read API keys from environment / ``.env`` and return a dict of clients.

    Keys present in the returned dict:
        ``"groq"``        – Groq client, or ``None`` if key missing.
        ``"openrouter"``  – OpenRouter client, or ``None`` if key missing.
        ``"gemini"``      – Gemini client, or ``None`` if key missing.

    Args:
        load_env: If ``True`` (default), call ``load_dotenv(override=True)``
                  before reading environment variables.

    Returns:
        Dict mapping provider name → ``OpenAI`` instance (or ``None``).
    """
    if load_env:
        load_dotenv(override=True)

    groq_key       = os.getenv("GROQ_API_KEY")
    openrouter_key = os.getenv("OPENROUTER_API_KEY")
    gemini_key     = os.getenv("GOOGLE_API_KEY")

    clients: dict[str, OpenAI | None] = {
        "groq":       None,
        "openrouter": None,
        "gemini":     None,
    }

    if groq_key:
        clients["groq"] = OpenAI(api_key=groq_key, base_url=GROQ_URL)

    if openrouter_key:
        clients["openrouter"] = OpenAI(api_key=openrouter_key, base_url=OPENROUTER_URL)

    if gemini_key:
        clients["gemini"] = OpenAI(api_key=gemini_key, base_url=GEMINI_URL)

    return clients


def call_llm(
    client: OpenAI,
    model: str,
    messages: list[dict],
    strip_markers: tuple[str, ...] = (
        "```cpp", "```c++", "```rust", "```go", "```python", "```",
    ),
) -> str:
    """
    Send *messages* to *client* using *model* and return the text reply.

    Markdown fences are stripped automatically because some models emit them
    despite explicit instructions not to.

    Args:
        client:        An ``openai.OpenAI`` instance pointing at any provider.
        model:         Model identifier string (provider-specific).
        messages:      Chat message list in OpenAI format.
        strip_markers: Fence tokens to remove from the reply.

    Returns:
        Cleaned text response from the model.
    """
    response = client.chat.completions.create(model=model, messages=messages)
    reply: str = response.choices[0].message.content or ""
    for marker in strip_markers:
        reply = reply.replace(marker, "")
    return reply.strip()


def check_required_keys(
    required: list[str],
    load_env: bool = True,
) -> dict[str, str | None]:
    """
    Load ``.env`` and return a dict of ``{env_var: value_or_None}``.

    Raises:
        EnvironmentError: if any key in *required* is missing.
    """
    if load_env:
        load_dotenv(override=True)

    values = {k: os.getenv(k) for k in required}
    missing = [k for k, v in values.items() if not v]
    if missing:
        raise EnvironmentError(
            f"Missing API key(s) in .env: {', '.join(missing)}\n"
            "Add them to your .env file and restart the kernel."
        )
    return values