import streamlit as st
from textwrap import dedent
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.youtube import YouTubeTools
import os

load_dotenv()

st.set_page_config(
    page_title="YouTube Analyzer • techwithronak",
    page_icon="▶️",
    layout="centered",
)

# Load CSS from file
def load_css():
    css_path = os.path.join(os.path.dirname(__file__), "style.css")
    with open(css_path) as f:
        css = f.read()
    st.markdown(
        f'<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">'
        f'<style>{css}</style>',
        unsafe_allow_html=True
    )

load_css()

# Top bar
st.markdown("""
<div class="top-bar">
    <div class="top-bar-left">
        <div style="width:38px;height:38px;background:#1a1a2e;border-radius:50%;display:flex;align-items:center;justify-content:center;color:white;font-weight:800;font-size:13px;">&lt;/&gt;</div>
        <span class="handle">@techwithronak</span>
        <div class="verified">&#10003;</div>
    </div>
    <div class="badge-pill">YouTube AI Agent</div>
</div>
""", unsafe_allow_html=True)

# Hero
st.markdown("""
<div class="hero">
    <div class="sparks">&#10022; &#10022;</div>
    <h1 class="hero-title">YouTube<br>   Analyzer</h1>
    <p class="hero-sub">
        Drop any YouTube link &mdash; get <span class="accent">AI-powered</span> timestamps,<br>
        summaries &amp; structured content breakdown.
    </p>
</div>
""", unsafe_allow_html=True)

# Input
url = st.text_input("🔗 YouTube Video URL", placeholder="https://www.youtube.com/watch?v=...")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    analyze_btn = st.button("🔥 Analyze Video")

# Tip bar
st.markdown("""
<div class="tip-bar">
    <div class="tip-icon">&#128161;</div>
    <span>Works best with videos that have
    <span style="color:#2D5BE3;font-weight:600;">auto-generated or manual captions</span> enabled.</span>
</div>
""", unsafe_allow_html=True)

st.divider()

# Agent
@st.cache_resource
def build_agent():
    return Agent(
        name="YouTube Agent",
        model=Groq(id="qwen/qwen3-32b"),
        tools=[YouTubeTools()],
        instructions=dedent("""\
            You are an expert YouTube content analyst with a keen eye for detail!
            Follow these steps for comprehensive video analysis:
            1. Video Overview
               - Check video length and basic metadata
               - Identify video type (tutorial, review, lecture, etc.)
               - Note the content structure
            2. Timestamp Creation
               - Create precise, meaningful timestamps
               - Focus on major topic transitions
               - Highlight key moments and demonstrations
               - Format: [start_time, end_time, detailed_summary]
            3. Content Organization
               - Group related segments
               - Identify main themes
               - Track topic progression
            Quality Guidelines:
            - Verify timestamp accuracy
            - Avoid timestamp hallucination
            - Ensure comprehensive coverage
        """),
        add_datetime_to_context=True,
        markdown=True,
    )

if analyze_btn:
    if not url.strip():
        st.warning("Please paste a YouTube URL first.")
    elif "youtube.com" not in url and "youtu.be" not in url:
        st.error("That doesn't look like a valid YouTube link.")
    else:
        agent = build_agent()

        st.markdown("""
        <div class="result-header">
            <div class="result-dot">&#128203;</div>
            <div class="result-title">Analysis Result</div>
        </div>
        """, unsafe_allow_html=True)

        result_placeholder = st.empty()
        full_response = ""

        with st.spinner("Analyzing your video..."):
            try:
                for chunk in agent.run(
                    f"Analyze this video: {url.strip()}",
                    stream=True,
                ):
                    if hasattr(chunk, "content") and chunk.content:
                        full_response += chunk.content
                        result_placeholder.markdown(full_response)
            except Exception as e:
                st.error(f"Something went wrong: {e}")

        if full_response:
            st.success("Analysis complete!")
            st.download_button(
                label="Download Analysis (.md)",
                data=full_response,
                file_name="youtube_analysis.md",
                mime="text/markdown",
            )

# Footer
st.markdown("""
<div class="footer">
    Built by
    <a href="https://github.com/ronakrajput8882" target="_blank">@techwithronak</a>
    &nbsp;&middot;&nbsp;
    <a href="https://www.linkedin.com/in/ronakrajput8882/" target="_blank">LinkedIn</a>
</div>
""", unsafe_allow_html=True)
