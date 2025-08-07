# YouTube Video Summarizer

This project allows you to automatically fetch the transcript of a YouTube video and generate a summary using an AI model. It uses the [`youtube-transcript-api`](https://github.com/jdepoix/youtube-transcript-api) to extract transcripts and the [OpenRouter API](https://openrouter.ai/) to summarize the content.

## Features

- Extracts transcripts from YouTube videos (including auto-generated ones, if available)
- Summarizes the transcript using an AI model (Qwen 2.5 7B Instruct via OpenRouter)
- Simple and extensible codebase

## Requirements

- Python 3.8+
- [youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/)
- [openai](https://pypi.org/project/openai/) (for OpenRouter API usage)

Install dependencies:
```bash
pip install youtube-transcript-api openai
```

## Usage

1. **Clone or download this repository.**
2. **Open `video_summarizer.ipynb` in VS Code or Jupyter Notebook.**
3. **Edit the YouTube URL in the code cell:**
   ```python
   video_id = get_video_id("https://www.youtube.com/watch?v=YOUR_VIDEO_ID")
   ```
4. **(Optional) Select transcript language:**  
   You can specify the transcript language by passing a language code (e.g., `'en'`, `'es'`) to the transcript function:
   ```python
   transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
   ```
5. **Run all cells.**
   - The transcript will be fetched and printed.
   - The summary will be generated and displayed.

### Example Output

```
Transcript fetched successfully.
Summary: [AI-generated summary of the video]
```

## Troubleshooting

- If you see errors about missing transcript methods, update the `youtube-transcript-api`:
  ```bash
  pip install --upgrade youtube-transcript-api
  ```
- Some videos may not have transcripts due to YouTube restrictions.
- Make sure your OpenRouter API key is valid.

## How It Works

1. **Extract Video ID:**  
   The `get_video_id` function parses the YouTube URL to get the video ID.

2. **Fetch Transcript:**  
   The `get_transcript` function uses the video ID to fetch the transcript. It prints available transcripts and joins all segments into a single string.

3. **Summarize Transcript:**  
   The transcript is sent to the OpenRouter API, which returns a summary.

## Contributing & Suggestions

If you have ideas for improvements, please open an issue or submit a pull request!  
Possible improvements include:
- Support for more AI models or providers
- Better error handling and user feedback
- Option to save summaries to a file
- Web or GUI interface
- **Option to select transcript language before fetching** (e.g., allowing users to specify `'en'`, `'es'`, etc.)

Your feedback is welcome!

## License

This project is for educational purposes. Please respect YouTube's and OpenRouter's