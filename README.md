<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,12,24&height=200&section=header&text=▶️%20YouTube%20AI%20Analyzer&fontSize=48&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=AI-Powered%20YouTube%20Video%20Analysis%20Agent&descAlignY=60&descAlign=50" width="100%"/>

<div align="center">
  
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Groq](https://img.shields.io/badge/Groq-LLM-00A67E?style=for-the-badge&logo=groq&logoColor=white)](https://groq.com)
[![Agno](https://img.shields.io/badge/Agno-Agent%20Framework-6C47FF?style=for-the-badge)](https://github.com/agno-agi/agno)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)

</div>

---

## 📌 Project Overview

**YouTube AI Analyzer** is an AI-powered agent that takes any YouTube video URL and returns a structured, timestamped content breakdown — including video type identification, segment summaries, topic progression, and key learning points.

Built with the **Agno** agent framework, powered by **Groq's Qwen3-32B** LLM, and wrapped in a fully branded **Streamlit** UI — no OpenAI API needed, entirely free to run.

> 🎯 **Use Case:** Students, content creators, and researchers who want instant structured summaries of long YouTube videos without watching the full content.

---

## 🧠 Agent Architecture

```
YouTube URL → Agno Agent → Groq (Qwen3-32B) → YouTubeTools (transcript fetch) → Structured Analysis → Streamlit UI
```

### How It Works

**1️⃣ URL Intake**
- User pastes any YouTube video URL into the Streamlit UI
- Input validated for correct YouTube domain format

**2️⃣ Transcript Extraction**
- `YouTubeTools` from Agno fetches the auto-generated or manual caption transcript
- Handles both `youtube.com` and `youtu.be` short URLs

**3️⃣ LLM Analysis via Groq**
- Transcript sent to `qwen/qwen3-32b` running on Groq's ultra-fast inference
- Agent follows structured instructions: Video Overview → Timestamp Creation → Content Organization

**4️⃣ Streaming Output**
- Response streamed token-by-token back to the UI in real time
- Final output downloadable as `.md` file

---

## 📊 Output Format

The agent produces a structured markdown report containing:

| Section | Description |
|:---|:---|
| 🎬 Video Overview | Title, type, length, structure |
| ⏱️ Timestamps | `[start, end]` with detailed segment summary |
| 📚 Key Learning Points | Bullet list of main takeaways |
| 🔗 References | Notable links or resources mentioned |

---

## 🔍 Key Insights

- **Groq inference** is 10–20× faster than standard OpenAI API — ideal for long transcripts
- **Qwen3-32B** handles multilingual transcripts better than smaller models
- `YouTubeTools` works on any video with captions (auto-generated or manual)
- Streaming output keeps UX snappy even for 1-hour long videos
- CSS-file separation from Streamlit logic prevents raw HTML leaking issues

---

## 🗂️ Repository Structure

```
youtube-ai-analyzer/
├── ui.py                  # Streamlit frontend
├── style.css              # Custom UI styles (instapost brand theme)
├── .env                   # API keys (not committed)
├── requirements.txt       # Dependencies
├── .streamlit/
│   └── config.toml        # Streamlit server config
└── README.md
```

---

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/ronakrajput8882/Youtube-Video-Analyzer.git
cd Youtube-Video-Analyzer

# 2. Install dependencies
pip install streamlit agno groq python-dotenv youtube-transcript-api

# 3. Set up API key
echo "GROQ_API_KEY=your_groq_key_here" > .env

# 4. Run the app
streamlit run ui.py
```

Get your free Groq API key at → [console.groq.com](https://console.groq.com)

---

## 🧠 Key Learnings

- Agno's `Agent` abstraction simplifies tool-augmented LLM calls to a few lines
- Groq's free tier supports Qwen3-32B with generous rate limits — no cost to run
- Streamlit CSS injection must use hardcoded hex values — CSS variables from `:root` don't resolve inside Streamlit's shadow DOM
- Separating CSS into `style.css` and loading via `open()` prevents raw HTML render bugs
- `@st.cache_resource` is critical — without it the agent re-initializes on every button click

---

## 🛠️ Tech Stack

| Tool | Purpose |
|:---|:---|
| Python 3.10+ | Core language |
| Streamlit 1.57 | Web UI framework |
| Agno | AI agent framework |
| Groq API | LLM inference (Qwen3-32B) |
| YouTubeTools | Transcript extraction |
| python-dotenv | Environment variable management |
| youtube-transcript-api | YouTube caption fetching |

---

<div align="center">

### Connect with me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/ronaksinh-rajput8882)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/techwithronak)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ronakrajput8882)

*If you found this useful, please ⭐ the repo!*

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,12,24&height=100&section=footer" width="100%"/>

</div>
