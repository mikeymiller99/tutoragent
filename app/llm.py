import json
from typing import List, Dict, Any, Optional
from openai import OpenAI

from app.config import OPENAI_API_KEY

_client: Optional[OpenAI] = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None


class LLMError(RuntimeError):
    pass


def call_llm_json(
    model: str,
    messages: List[Dict[str, str]],
    temperature: float = 0.2,
) -> Dict[str, Any]:
    """
    Single gateway for all LLM calls.
    Enforces JSON-only responses and throws clear errors on invalid outputs.
    """
    if _client is None:
        raise LLMError("OPENAI_API_KEY is not set. Add it to .env or Codespaces secrets and restart.")

    resp = _client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        response_format={"type": "json_object"},
    )

    content = resp.choices[0].message.content or ""
    try:
        return json.loads(content)
    except Exception as e:
        raise LLMError(f"Model did not return valid JSON. Raw output: {content}") from e
