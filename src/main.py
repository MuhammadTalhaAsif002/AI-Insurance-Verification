import os
import json
from pathlib import Path
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

BASE_DIR = Path(__file__).resolve().parent.parent

input_file = BASE_DIR / "data" / "input" / "sample_note_01.txt"
prompt_file = BASE_DIR / "prompts" / "verification_prompt.txt"
output_dir = BASE_DIR / "data" / "output"

output_dir.mkdir(parents=True, exist_ok=True)

with open(input_file, "r", encoding="utf-8") as f:
    insurance_note = f.read()

with open(prompt_file, "r", encoding="utf-8") as f:
    system_prompt = f.read()

message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=2000,
    system=system_prompt,
    messages=[
        {
            "role": "user",
            "content": insurance_note
        }
    ]
)

response_text = message.content[0].text

# Convert Claude's response into JSON
result = json.loads(response_text)

output_file = output_dir / "sample_note_01.json"

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4)

print("Insurance verification completed.")
print(f"Output saved to: {output_file}")