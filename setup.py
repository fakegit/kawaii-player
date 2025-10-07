"""
Copyright (C) 2017 kanishka-linux kanishka.linux@gmail.com

This file is part of kawaii-player.

kawaii-player is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

kawaii-player is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with kawaii-player.  If not, see <http://www.gnu.org/licenses/>.
"""


import os
import shutil
import platform
from setuptools import Extension, setup
from Cython.Build import cythonize
import ctypes.util

system = platform.system().lower()

"""
 GNU/Linux users should install dependencies manually using their native
 package manager
"""

install_requires = []
if system in ["darwin", "nt"]:
    install_requires = [
        "PyQt5",
        "pycurl",
        "bs4",
        "Pillow",
        "mutagen",
        "lxml",
        "yt-dlp",
        "certifi",
        "PyQtWebEngine",
        "PyOpenGL",
        "python-vlc"
    ]

library_path = None
if system == "darwin":
    library_path = ["/usr/local/lib"]

extension_src = "pympv/mpv.pyx"

if library_path is None:
    extensions = [Extension("mpv", [extension_src], libraries=["mpv"])]
else:
    extensions = [Extension("mpv", [extension_src], libraries=["mpv"], library_dirs=library_path)]

setup(
    name='kawaii-player',
    version='6.0.0',
    license='GPLv3',
    author='kanishka-linux',
    author_email='kanishka.linux@gmail.com',
    url='https://github.com/kanishka-linux/kawaii-player',
    long_description="README.md",
    packages=[
        'kawaii_player', 'kawaii_player.Plugins', 'kawaii_player.widgets',
        'kawaii_player.hls_webengine', 'kawaii_player.hls_webkit',
        'kawaii_player.vinanti', 'kawaii_player.tvdb_async',
        ],
    include_package_data=True,
    install_requires = install_requires,
    ext_modules = cythonize(extensions, force=True),
    entry_points={
        'gui_scripts':['kawaii-player = kawaii_player.kawaii_player:main'], 
        'console_scripts':['kawaii-player-console = kawaii_player.kawaii_player:main']
        }, 
    description="A Audio/Video manager, multimedia player and portable media server",
)
