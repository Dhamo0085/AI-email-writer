# ✉️ Professional Email Generator

An AI-powered tool that generates polished, professional emails based on your inputs. Built during the AI Integration & Innovation Bootcamp at Northeastern University.

## 🎯 What It Does

- Takes structured inputs (sender, recipient, purpose, tone, etc.)
- Generates professional emails using OpenAI's GPT models
- Offers quick templates for common scenarios (networking, research assistantship, thank you notes)
- Demonstrates prompt engineering principles in action

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
## API Setup: Google Gemini (Recommended)

**Why Gemini?**
- ✅ **Free tier:** 60 requests/min (vs OpenAI's 3/min)
- ✅ **No credit card** required
- ✅ **High quality** outputs
- ✅ **Perfect for learning**

**Get Your Free API Key:**

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with Google account
3. Click "Get API Key"
4. Create new project or use existing
5. Copy the key (starts with `AIza...`)
6. Add to `.env`:
```
   GEMINI_API_KEY=AIzaSyXXXXXXXXXXXXXXX
```

**Alternative: OpenAI**

If you prefer OpenAI (requires credit card after free trial):
1. Get key from [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Add to `.env`: `OPENAI_API_KEY=sk-proj-...`
3. Uncomment OpenAI code in `app.py`
```

---

## **FOR YOUR SESSION 3 STUDENTS**

Update your session email:
```
Important Update: We're using Google Gemini API (Free!)

Instead of OpenAI, we'll use Google's Gemini API which has:
- 60 requests/min (vs OpenAI's 3/min on free tier)
- No credit card required
- Better for learning and experimentation

Get your FREE API key before class:
https://makersuite.google.com/app/apikey

### Installation

1. **Clone or download this repository**
```bash
git clone <repository-url>
cd professional-email-generator
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up your API key**

   - Copy `.env.example` to `.env`:
```bash
   cp .env.example .env
```
   
   - Open `.env` and replace `your_api_key_here` with your actual OpenAI API key:
```
   OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxx
```

4. **Run the app**
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📖 How to Use

1. **Fill out the form** in the sidebar:
   - Your name and role
   - Recipient's name and role
   - Purpose of the email
   - Background context (optional)
   - Tone (Professional, Formal, Friendly, Persuasive)
   - Desired length
   - Key points to include

2. **Choose a template** (optional):
   - Research Assistantship
   - Networking
   - Thank You
   - Follow-Up
   - Or use "Custom"

3. **Click "Generate Email"**

4. **Review and copy** the generated email

5. **Regenerate** if you want a different version

## 🛠️ Project Structure
```
professional-email-generator/
├── app.py              # Main Streamlit application
├── prompts.py          # Email prompt templates and builder
├── requirements.txt    # Python dependencies
├── .env.example        # Example environment variables
├── .env               # Your API keys (DO NOT COMMIT)
├── .gitignore         # Git ignore file
└── README.md          # This file
```

## 🧠 How It Works (Prompt Engineering)

This tool demonstrates the **RCFC Framework** from Session 2:

- **Role**: "You are a professional email writing assistant"
- **Context**: Sender, recipient, purpose, background
- **Format**: Subject line, greeting, body, closing, signature
- **Constraints**: Tone, length, key points to include

The `prompts.py` file shows how to programmatically build structured prompts that produce high-quality AI outputs.

## 🔧 Customization Ideas (For Your Final Project)

Extend this tool by adding:

- **More templates**: Job applications, apologies, cold outreach, rejection follow-ups
- **LinkedIn post generator**: Same pattern, different output format
- **Cover letter writer**: Upload resume, generate tailored cover letters
- **Multi-language support**: Generate emails in Spanish, Mandarin, etc.
- **Email sentiment analyzer**: Classify the tone of incoming emails
- **Email thread summarizer**: Summarize long email chains
- **A/B testing**: Generate 2-3 versions and let user choose
- **Email history**: Save and retrieve past generated emails
- **Integration**: Connect to Gmail API to send directly

## 🔐 API Key Security

**IMPORTANT:**

- Never commit your `.env` file to GitHub
- Never share your API key publicly
- The `.gitignore` file prevents `.env` from being committed
- If you accidentally expose your key, regenerate it immediately at [OpenAI](https://platform.openai.com/api-keys)

## 💰 API Costs

- **GPT-3.5-turbo**: ~$0.0015 per email (very cheap)
- **GPT-4**: ~$0.03 per email (more expensive, higher quality)

For this bootcamp project, GPT-3.5-turbo is recommended.

## 🐛 Troubleshooting

### "Module not found" error
```bash
pip install -r requirements.txt
```

### "Invalid API key" error

- Check that your `.env` file exists in the project root
- Verify your API key is correct (starts with `sk-proj-` or `sk-`)
- Make sure there are no extra spaces in `.env`

### App won't start
```bash
# Try running with verbose output
streamlit run app.py --logger.level=debug
```

### API rate limit errors

- You're making too many requests too quickly
- Wait a few seconds between generations
- Consider upgrading your OpenAI plan

## 📚 Resources

**Prompt Engineering:**
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Learn Prompting](https://learnprompting.org)

**Streamlit:**
- [Streamlit Documentation](https://docs.streamlit.io)
- [Streamlit Gallery](https://streamlit.io/gallery)

**OpenAI API:**
- [API Reference](https://platform.openai.com/docs/api-reference)
- [Usage Dashboard](https://platform.openai.com/usage)

## 🎓 Learning Outcomes

By building this project, you've learned:

✅ How to structure prompts programmatically (RCFC framework)  
✅ How to integrate OpenAI API into a Python application  
✅ How to build interactive UIs with Streamlit  
✅ How to handle user inputs and generate dynamic outputs  
✅ How to manage API keys securely  
✅ How to structure a real-world AI application  

## 📝 License

This project is for educational purposes as part of the AI Integration & Innovation Bootcamp at Northeastern University.

## 🙋 Questions?

- **Instructor**: Dhamodaran Selvam
- **Discord**: [Channel Link]
- **Email**: [Your Email]

## 🌟 Acknowledgments

Built during Session 3 of the AI Integration & Innovation Bootcamp, February 2026.

Special thanks to all bootcamp participants for their engagement and feedback!

---

**Happy Emailing! ✉️**