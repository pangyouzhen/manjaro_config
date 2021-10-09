FROM manjarolinux/base:latest
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"

RUN \
    pacman-mirrors -c China \
    && cat /etc/pacman.d/mirrorlist \
    && sudo pacman -Syuu --noconfirm   \
    && sudo pacman -S --noconfirm base-devel \
#    && yes y | sudo pacman -S wget \
#    && yes y | yay -S miniconda \
#    && yes y | sudo pacman -Syuu \
#    && yes y | sudo pacman -S python \
#    && yes y | sudo pacman -S yay \
#    && yes y | sudo pacman -S git \
#    && yes y | sudo pacman -S docker \
#    && yay -Ss pycharm | grep profession | xargs yay -S \