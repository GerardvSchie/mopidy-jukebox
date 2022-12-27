#!/bin/bash

cd "${0%/*}"

chmod 022
pip install build
python3 -m build
pip install dist/Mopidy-Jukebox-0.1.0.tar.gz
