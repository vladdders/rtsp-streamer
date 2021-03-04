import gi

gi.require_version('Gst', '1.0')
gi.require_version('GstRtspServer', '1.0')
from gi.repository import Gst, GstRtspServer, GLib


PATH_TO_VIDEO = ""
PATH_TO_VIDEO2 = ""
PATH_TO_VIDEO3 = ""


PATHS = [PATH_TO_VIDEO, PATH_TO_VIDEO2, PATH_TO_VIDEO3]

loop = GLib.MainLoop()
Gst.init(None)


class TestRtspMediaFactory(GstRtspServer.RTSPMediaFactory):
    def __init__(self, path_to_video):
        super(TestRtspMediaFactory, self).__init__()
        self.path_to_video = path_to_video

    def do_create_element(self, url):

        #set mp4 file path to filesrc's location property
        src_demux = f"filesrc location={self.path_to_video} ! qtdemux name=demux"

        h264_transcode = "demux.video_0"
        # uncomment following line if video transcoding is necessary
        h264_transcode = "demux.video_0 ! decodebin ! queue ! x264enc"
        pipeline = "{0} {1} ! queue ! rtph264pay name=pay0 config-interval=1 pt=96".format(src_demux, h264_transcode)
        print ("Element created: " + pipeline)
        return Gst.parse_launch(pipeline)


class GstreamerRtspServer():
    def __init__(self):

        self.rtspServer = GstRtspServer.RTSPServer()
        
        factories = [TestRtspMediaFactory(pth) for pth in PATHS]

        for i, factory in enumerate(factories):
            factory.set_shared(True)
            mountPoints = self.rtspServer.get_mount_points()
            mountPoints.add_factory(f"/stream{i}", factory)

        self.rtspServer.attach(None)


if __name__ == '__main__':
    s = GstreamerRtspServer()
    loop.run()
