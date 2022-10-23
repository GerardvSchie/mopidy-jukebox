import logging

import pykka

from mopidy import backend

from mopidy_jukebox import storage
from mopidy_jukebox.library import LocalLibraryProvider
from mopidy_jukebox.playback import LocalPlaybackProvider

logger = logging.getLogger(__name__)


class LocalBackend(pykka.ThreadingActor, backend.Backend):
    uri_schemes = ["jukebox"]

    def __init__(self, config, audio):
        super().__init__()

        self.config = config

        storage.check_dirs_and_files(config)

        self.playback = LocalPlaybackProvider(audio=audio, backend=self)
        self.library = LocalLibraryProvider(backend=self, config=config)
