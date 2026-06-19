import streamlit as st
import yt_dlp
import os
import uuid

st.title("📥 Facebook Reels Downloader (Public / Allowed Only)")

st.warning(
    "This tool downloads *only publicly accessible* Facebook videos. "
    "It cannot and will not bypass login walls or protected content."
)

url = st.text_input("Enter Facebook Reel URL")

def download_video(video_url):
    video_id = str(uuid.uuid4())
    output_path = f"downloads/{video_id}.mp4"
    os.makedirs("downloads", exist_ok=True)

    ydl_opts = {
        "outtmpl": output_path,
        "format": "best",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    return output_path

if st.button("Download"):
    if not url:
        st.error("Please enter a valid Facebook Reels URL.")
    else:
        try:
            filepath = download_video(url)
            st.success("Download complete!")
            
            with open(filepath, "rb") as f:
                st.download_button(
                    label="Download Reel",
                    data=f,
                    file_name="facebook_reel.mp4",
                    mime="video/mp4",
                )
        except Exception as e:
            st.error(f"Could not download video: {e}")
