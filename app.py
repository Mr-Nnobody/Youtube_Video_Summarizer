import streamlit as st
import os
from youtube_transcript_api import YouTubeTranscriptApi
import openai

# Set your OpenRouter API Key
API_KEY = os.getenv("OPENROUTER_API_KEY")

# Streamlit application
st.title('YouTube Video Summarizer')

video_url = st.text_input('Enter YouTube video URL:')

if video_url:
    # Extract video ID from URL
    video_id = video_url.split('v=')[-1].split('&')[0]
    
    try:
        # Fetch transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = ' '.join([t['text'] for t in transcript])
        st.write(transcript_text)
        
        # Summarize transcript
        response = openai.Completion.create(
            engine="davinci",
            prompt=transcript_text,
            api_key=API_KEY
        )
        summary = response.choices[0].text.strip()
        st.write('Summary:')
        st.write(summary)
    except Exception as e:
        st.error(f'Error: {str(e)}')
