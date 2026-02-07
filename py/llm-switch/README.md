# LLM Switch Project (Claude ↔ GPT)

This project demonstrates how to **switch between Claude (Anthropic) and GPT (OpenAI) using configuration only**, without changing business code.

## Features
- Config-based LLM provider switch
- Clean factory pattern
- Enterprise-ready structure
- Easy to extend (FastAPI / .NET equivalent)

---

## Project Structure
```
llm-switch/
│
├── config.yaml          # Switch provider here
├── claude_client.py     # Claude implementation
├── gpt_client.py        # GPT implementation
├── llm_factory.py       # LLM switch logic
├── main.py              # Application entry point
├── requirements.txt
└── README.md
```

---

## Prerequisites
- Python 3.9+
- Anthropic API key
- OpenAI API key

---

## Setup Steps

### 1. Unzip project
```bash
unzip llm-switch-project.zip
cd llm-switch
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set API keys

#### Linux / Mac
```bash
export ANTHROPIC_API_KEY="your_claude_key"
export OPENAI_API_KEY="your_openai_key"
```

#### Windows (PowerShell)
```powershell
setx ANTHROPIC_API_KEY "your_claude_key"
setx OPENAI_API_KEY "your_openai_key"
```

---

## Run the project
```bash
python main.py
```

You will see the LLM response printed in the console.

---

## Switch Claude ↔ GPT
Open `config.yaml` and change:
```yaml
provider: anthropic
```
to:
```yaml
provider: openai
```

Run again:
```bash
python main.py
```

No code changes required.

---

## Architecture Explanation
- `llm_factory.py` decides which LLM to call
- Business code remains LLM-agnostic
- Providers can be added easily

---

## Interview-ready explanation
> "We abstract LLM providers behind a factory and switch them via configuration to avoid vendor lock-in."

---

## Next Improvements
- Add FastAPI REST layer
- Add retry & fallback
- Add logging & metrics
- Port same design to .NET with DI

---

Happy Learning 🚀
