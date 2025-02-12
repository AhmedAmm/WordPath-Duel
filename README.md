# WordPath-Duel

A Python-based AI search game built with Pygame.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/AhmedAmm/WordPath-Duel
   cd WordPath-Duel
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your API key:
   - Visit [OpenRouter](https://openrouter.ai/) and sign up.
   - Generate an API key from your OpenRouter account.
   - Create a `.env` file in the project root and add the following line:
     ```ini
     OPENROUTER_API_KEY=your_api_key_here
     ```
4. Run the application:
   ```bash
   python main.py
   ```

## Requirements
- Python 3.7+
- Pygame 2.6.1

## Environment Variables
This project uses an API key stored in a `.env` file. Ensure you have the `python-dotenv` package installed, as listed in `requirements.txt`, to load environment variables securely.

## Dependencies
The required dependencies are listed in `requirements.txt`:
```
annotated-types==0.7.0
anyio==4.8.0
certifi==2025.1.31
distro==1.9.0
h11==0.14.0
httpcore==1.0.7
httpx==0.28.1
idna==3.10
jiter==0.8.2
openai==1.61.1
pydantic==2.10.6
pydantic_core==2.27.2
pygame==2.6.1
python-dotenv==1.0.1
sniffio==1.3.1
tqdm==4.67.1
typing_extensions==4.12.2
