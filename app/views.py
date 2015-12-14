from __future__ import unicode_literals
from django.shortcuts import redirect

import youtube_dl

# HTTP 302 to the 'real' video URL of the highest quality available
# for the youtube video with the 'v' query parameter.
# For example,
# /?v=spOq3wIO9mk will resolve to a michael jackson video mp4 :)
def index(request):
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'forceurl': True,
        'skip_download': True
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        youtube_video_id = request.GET["v"]
        youtube_video_file_url = ydl.extract_info(youtube_video_id, download = False)['url']
        return redirect(youtube_video_file_url)