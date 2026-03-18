import streamlit as st
import os
from youtube_transcript_api import YouTubeTranscriptApi
import openai

# Set your OpenRouter API Key
API_KEY = os.getenv("OPENROUTER_API_KEY")
def get_transcript(video_id):
    try:
        # List all available transcripts
        ytt_api = YouTubeTranscriptApi()
        transcript_list = ytt_api.list(video_id)
        print("Available transcripts:", transcript_list)

        # Get the default transcript
        fetched_transcript = ytt_api.fetch(video_id)
        joined_transcript = " ".join([segment.text for segment in fetched_transcript])
        print("Transcript fetched successfully.")
    except Exception as e:
        print(f"Error Could not retrieve any transcript for this video.: {e}")
        return []
    return joined_transcript

# Streamlit application
st.title('YouTube Video Summarizer')

video_url = st.text_input('Enter YouTube video URL:')
if video_url:
    # Extract video ID from URL
    video_id = video_url.split('v=')[-1].split('&')[0]
    
    try:
        # Fetch transcript
        transcript_text = get_transcript(video_id)
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
