<h1>RTSP streaming server</h1>

A RTSP streamer that serves a video saved to disk. It's based on 
[this](https://stackoverflow.com/questions/59858898/how-to-convert-a-video-on-disk-to-a-rtsp-stream).
I add here all the necessary steps to actually prepare the running environment.

<h2>Installation</h2>

```
sudo apt-get install libgstreamer1.0-0 gstreamer1.0-plugins-base 
gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly 
gstreamer1.0-libav gstreamer1.0-doc gstreamer1.0-tools gstreamer1.0-x 
gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio
```

```
sudo apt-get install python3-gi
```

```
sudo apt-get install gir1.2-gst-rtsp-server-1.0
```

Set the absolute path to video in variable `PATH_TO_VIDEO` in `feed.py`.

```
python feed.py
```

To watch the video you can install `opencv-python` in your environment and run `access-rtsp.py` or use
vlc for instance with the link: `rtsp://localhost:8554/stream1`.