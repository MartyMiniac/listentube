# listentube
A webserver based on youtube-dl to listen youtube audios
<br>
[Here is the Website Link](https://listentube.herokuapp.com/)

## What is it ?
It is quite frustating when you want to jus here just a youtube video. Think about a music video of which you just want to here the music or a podcast of which you just want voice and no video stream. So here is the deal! How about streaming just audio and no video and if you like it why not download it from the same place. This is a heroku deployable webserver based on flask which accepts youtube url as requests and returns you an audio streaming page where you can stream the audio.

## How to Use ?

### First Page

![Image showing the Index Page](https://github.com/MartyMiniac/listentube/blob/master/images/index_page.JPG "Index Page")

This is the first page you will see when you open the app
<br>
Here you need to enter the url of the youtube video you want to listen
<br>
Please Follow this format `https://www.youtube.com/watch?v=*id of the youtube video*`
<br>
In future support for short notation will be added too.

### Audio Listening Page

![Image showing the Audio Listening Page](https://github.com/MartyMiniac/listentube/blob/master/images/listen_page.JPG "Audio Listening Page")

This is the page where you will be listening to the audio
<br>
By clicking the download button you will be able to download the audio file.

### Simple Trick

![Image showing the Audio Listening Page](https://github.com/MartyMiniac/listentube/blob/master/images/api.JPG "Audio Listening Page")

Here is a trick for you lazy pants.
<br>
You can add video id at the end of the url to directly land in the audio player with the audio loaded.
<br>
Follow the Format `https://listentube.herokuapp.com/*id of the youtube video to listen*`
<br>
<br>
**If you really Liked it don't forget to slap that star button and follow me on github for my upcoming projects**
