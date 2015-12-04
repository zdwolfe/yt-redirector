# yt-redirector

A simple web app to redirect to the raw video URL of a youtube video using the [youtube-dl](https://github.com/rg3/youtube-dl) python module.

## Why?
  [Zapier](https://zapier.com) can be used to respond to events (called triggers) that happen on one web app with actions on another web app. One of Zapier's [triggers](https://zapier.com/zapbook/youtube/) is upon a new YouTube video given some user. One available action is to make an RSS feed. So, ``yt-redirector`` connects the two, making RSS feeds of the raw video files of my favorite content creators on YouTube (which is auto-synced to my Android tablet) for those times I'm without an internet connection.

## Usage
Hit the app's URL, supplying a ```v``` query parameter that matches the youtube video id you want to be redirected to. For example, http://localhost:5000?v=spOq3wIO9mk will HTTP 302 redirect you to the source mp4 video file of  https://www.youtube.com/watch?v=spOq3wIO9mk (which I won't link directly to for obvious reasons).


## Installation
This is mostly just a hacked up [Heroku starter python app](https://devcenter.heroku.com/articles/getting-started-with-python), so follow the steps to install/deploy.

TL;DR: 

1. ``git clone git@github.com:zdwolfe/yt-redirector.git``
2. ``heroku create``
3. ``git push heroku master``
4. ``heroku ps:scale web=1``
