# Mopidy-Jukebox

Build and run the package using [script.sh](script.sh)

```
pip install build
```

```bash
python3 -m build
pip install dist/Mopidy-Jukebox-0.1.0.tar.gz
mopidy jukebox scan
```

Scan for list of plates
```bash
mopidy jukebox scan
```

Clear the list of plates
```bash
mopidy jukebox clear
```
