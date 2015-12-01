# youtube-dl-web

A simple redirector to redirect to the 'real' video (mp4) URL of a youtube video using the [youtube-dl](https://github.com/rg3/youtube-dl) python module.

This was meant to be used in with [Zapier](https://zapier.com) to automatically download YouTube videos into my DropBox account for those times I'm without an internet connection.


## Installation
This is mostly just a hacked up [Heroku starter python app](https://devcenter.heroku.com/articles/getting-started-with-python), so follow the steps to install/deploy.

## Usage
Hit the app's URL, supplying a ```v``` query parameter that matches the one you want to download. For example, http://localhost:5000?v=spOq3wIO9mk will HTTP 302 redirect you to the source video file of [Michael Jackson](https://www.youtube.com/watch?v=spOq3wIO9mk).
