FROM manjarolinux/base:latest
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"

# ？
#RUN useradd --create-home --no-log-init --shell /bin/bash docker \
#&& adduser docker sudo \
#&& echo 'docker:123456' | chpasswd
#
#USER docker:docker

RUN \
    pacman-mirrors -c China \
    && cat /etc/pacman.d/mirrorlist \
    && sudo pacman -Syuu --noconfirm   \
    && sudo pacman -S --noconfirm base-devel wget yay git docker \
    && yay -S --noconfirm typora miniconda3 pycharm-professional \