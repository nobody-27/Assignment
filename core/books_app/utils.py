import os
from django.conf import settings
from rest_framework.parsers import MultiPartParser
from moviepy.editor import ImageClip, CompositeVideoClip,AudioFileClip
import uuid

def handle_uploaded_image(uploaded_image):
    path = os.path.join(settings.MEDIA_ROOT, 'uploaded_images')
    if not os.path.exists(path):
        os.makedirs(path)

    image_path = os.path.join(path, uploaded_image.name)
    with open(image_path, 'wb+') as destination:
        for chunk in uploaded_image.chunks():
            destination.write(chunk)

    return image_path

def generate_video(image_path):
    clip = ImageClip(image_path, duration=5)
    file_name = 'generated_video' + str(uuid.uuid4())[:8]


    audio_path = os.path.join(settings.MEDIA_ROOT,'audio')
    
    # Load the audio clip
    # audio_clip = AudioFileClip(audio_path)

    video_path = os.path.join(settings.MEDIA_ROOT,'generated_videos', f'{file_name}.mp4')
    clip.write_videofile(video_path, codec="libx264", audio_codec="aac", fps=24)
    return video_path