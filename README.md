# Market Bot

## Setup and Running the Bot

### 1. Create and activate the virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate   # On macOS/Linux
# or
.\.venv\Scripts\activate    # On Windows PowerShell
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure your environment variables

Create a `.env` file in the project root directory with your Discord bot token:

```
SECRET_BOT_TOKEN=your_discord_bot_token_here
```

Make sure you have the `python-dotenv` package installed if you use `.env` files.

---

### 4. Running the bot

Run the bot module with:

```bash
python3 -m market_bot
```