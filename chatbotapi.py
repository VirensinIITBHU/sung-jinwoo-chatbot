
from openai import OpenAI
from dotenv import load_dotenv

import os
import asyncio
import tiktoken

from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential
)



# ---------------- LOAD ENV ----------------

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")
# ---------------- CLIENT ----------------

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


# ---------------- MEMORY WINDOW ----------------

MEMORY_WINDOW = 6




# ---------------- TOKENIZER ----------------

encoding = tiktoken.get_encoding("cl100k_base")

# ---------------- MEMORY ----------------

messages = [
    {
        "role": "system",
        "content": "You are a ANIME GEEK and you reply with harsh quotes and motivational lines, dont break your character, dont motivate me to be a anime fan too, use qoutes "
    }
]


# ---------------- STREAM FUNCTION ----------------

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10)
)

async def stream_ai_response(user_message):

    # save user message
    

    messages.append({
        "role": "user",
        "content": user_message
    })

    # ---------------- TOKEN COUNTING ----------------

    total_input_tokens = 0

    for msg in messages:

        total_input_tokens += len(
            encoding.encode(msg["content"])
        )

    print(f"\nInput Tokens: {total_input_tokens}")

    price_per_million = 0.10

    estimated_cost = (
        total_input_tokens / 1_000_000
    ) * price_per_million

    print(
        f"Estimated Input Cost: ${estimated_cost:.8f}"
    )
    # ---------------- TRIM MEMORY ----------------
    system_message = messages[0] 
    recent_messages = messages[-MEMORY_WINDOW:] 
    trimmed_messages = [ system_message, *recent_messages ]

    # ---------------- CREATE STREAM ----------------

    stream = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=trimmed_messages,
        stream=True,
        stream_options={"include_usage": True}
    )

    full_reply = ""
    usage_data = None

    # ---------------- STREAM LOOP ----------------

    try:

        for chunk in stream:

            # usage chunk sometimes has no choices

            if chunk.usage:
                usage_data = chunk.usage

            if not chunk.choices:
                continue

            content = chunk.choices[0].delta.content

            if content:

                full_reply += content

                # send chunk to FastAPI

                yield content

                await asyncio.sleep(0.03)

        # save assistant memory ONCE

        messages.append({
            "role": "assistant",
            "content": full_reply
        })

        # ---------------- TOKEN USAGE ----------------

        if usage_data:

            print("\n--- TOKEN USAGE ---")

            print(
                "Prompt Tokens:",
                usage_data.prompt_tokens
            )

            print(
                "Completion Tokens:",
                usage_data.completion_tokens
            )

            print(
                "Total Tokens:",
                usage_data.total_tokens
            )

    except Exception as e:

        print("\nERROR:", e)



