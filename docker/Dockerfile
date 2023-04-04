FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        ffmpeg \
        pulseaudio \
        wget \
        x11vnc \
        xvfb \
        && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /root/.config/obs-studio/plugins/linux-pulseaudio/

ADD https://github.com/obsproject/obs-studio/raw/master/plugins/linux-pulseaudio/bin/64bit/libpulseaudio.so /root/.config/obs-studio/plugins/linux-pulseaudio/

RUN apt-get update && apt-get install -y obs-studio

CMD ["/usr/bin/obs"]
