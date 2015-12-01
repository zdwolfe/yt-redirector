# youtube-dl-web

A simple redirector to redirect to the 'real' video (mp4) URL of a youtube video using the [youtube-dl](https://github.com/rg3/youtube-dl) python module.

This was meant to be used alongside [Zapier](https://zapier.com) to automatically download YouTube videos into my DropBox account (which is synced to my Android tablet) for those times I'm without an internet connection.


## Installation
This is mostly just a hacked up [Heroku starter python app](https://devcenter.heroku.com/articles/getting-started-with-python), so follow the steps to install/deploy.

## Usage
Hit the app's URL, supplying a ```v``` query parameter that matches the youtube video id you want to be redirected to. For example, http://localhost:5000?v=spOq3wIO9mk will HTTP 302 redirect you to the source mp4 video file of  https://www.youtube.com/watch?v=spOq3wIO9mk (which I won't link directly to for obvious reasons).
