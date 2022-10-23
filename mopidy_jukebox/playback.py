from mopidy import backend
import logging

from mopidy_jukebox import translator


class LocalPlaybackProvider(backend.PlaybackProvider):
    def translate_uri(self, uri):
        return translator.local_uri_to_file_uri(
            uri, self.backend.config["jukebox"]["media_dir"]
        )

    def pause(self) -> bool:
        """
        Pause playback.

        *MAY be reimplemented by subclass.*

        :rtype: :class:`True` if successful, else :class:`False`
        """
        logging.debug("PAUSE JUKEBOX")
        return self.audio.pause_playback().get()

    def play(self) -> bool:
        """
        Start playback.

        *MAY be reimplemented by subclass.*

        :rtype: :class:`True` if successful, else :class:`False`
        """
        logging.debug("PLAY JUKEBOX")
        return self.audio.start_playback().get()
