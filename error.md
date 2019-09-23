## 1.stream:安装pip install av 失败解决办法:
    Could not find libavformat with pkg-config.
    Could not find libavcodec with pkg-config.
    Could not find libavdevice with pkg-config.
    Could not find libavutil with pkg-config.
    Could not find libavfilter with pkg-config.
    Could not find libswscale with pkg-config.
    Could not find libswresample with pkg-config.

解决办法:
    sudo apt install \
    autoconf \
    automake \
    build-essential \
    cmake \
    libass-dev \
    libfreetype6-dev \
    libjpeg-dev \
    libtheora-dev \
    libtool \
    libvorbis-dev \
    libx264-dev \
    pkg-config \
    wget \
    yasm \
    zlib1g-dev

wget http://ffmpeg.org/releases/ffmpeg-3.2.tar.bz2
tar -xjf ffmpeg-3.2.tar.bz2
cd ffmpeg-3.2

./configure --disable-static --enable-shared --disable-doc
make
sudo make install

pip install av

## 2.可选stream安装
   sudo apt-get install -y python-dev pkg-config libavformat-dev libavcodec-dev libavdevice-dev libavutil-dev libswscale-dev libavresample-dev libavfilter-dev
Te
