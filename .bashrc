# https://github.com/rupa/z 启用z.sh 服务
#. ~/z.sh

if grep -q Microsoft /proc/version; then
    # wsl
    exe_program()
elif [[ "$UNAME" == CYGWIN* || "$UNAME" == MINGW* ]]; then
    # git bash == windows
    exe_program()
fi

exe_program(){
    # 映射linux wps的相关命令到windows
     alias et='/mnt/c/Program\ Files/Microsoft\ Office/root/Office16/EXCEL.EXE'
     alias wps='/mnt/c/Program\ Files/Microsoft\ Office/root/Office16/WINWORD.EXE'
     alias wpp='/mnt/c/Program\ Files/Microsoft\ Office/root/Office16/POWERPNT.EXE'
    # 映射linux资源管理器到windows
     alias thunar='explorer.exe'
}

lg() {
  #  lazygit
  git pull origin "$(git branch --show-current)"
  # 针对老版本git 没有 -show-current
  #git pull origin "$(git branch | grep '*' | awk '{print $2}')"
  # $? 是显示最后命令的退出状态
  if [ $? -eq 0 ]; then
    echo "-----pull success------- "
    git add .
    git commit -a -m "$1"
    git push origin "$(git branch --show-current)"
    echo "-----push success-------"
  fi
}

 port_path(){ 
  lsof -i:$1 | awk '{print $2}' | grep -v PID | xargs pwdx
 }

scp148(){
  scp $1 root@81.71.140.148:/tmp && ssh root@81.71.140.148
}

alias vv="virtualenv venv && source ./venv/bin/activate"
alias docker_remove_exit="docker ps -a | grep Exit | awk '{print \$1}' | xargs docker rm"
alias docker_restart="sudo systemctl restart docker && sudo chmod 666 /var/run/docker.sock"
alias docker_remove_none="docker images | grep none | awk '{print \$3}' | xargs docker rmi"
alias docker_remove="docker ps -a | grep Exit | awk '{print \$1}' | xargs docker rm && docker images | grep none | awk '{print \$3}' | xargs docker rmi"
alias ll="ls -alh"
#wget 断点续传
alias wget="wget -c"
#递归的创建目录
alias mkdir="mkdir -pv"
alias rsync-stock="rsync -avz root@81.71.140.148:/data/project/stock ./ --exclude venv --exclude __pycache__ --exclude .git --exclude .idea --exclude log"
alias s148="ssh root@81.71.140.148"
alias python="python3"
alias code="/opt/vscode/bin/code"
alias richeasy="sudo /usr/local/RichEZ/AppRun > /dev/null 2>&1 &"
alias v2raya='sudo v2raya > /dev/null 2>&1 &'

#  manjaro 下更新系统命令
Syuu (){
  sudo timeshift --create --comments $1 --snapshot-device /dev/sdb1 && sudo pacman -Syuu
}

http_proxy(){
  export http=http://127.0.0.1:$1
  export https=http://127.0.0.1:$1
}

git_proxy(){
  git config --global http.proxy socks5://127.0.0.1:$1
  git config --global https.proxy socks5://127.0.0.1:$1
  git config --global http.sslVerify false
}

cp2king(){
  # 挂载并复制文件到金士顿u盘
  sudo mount /dev/sdc1 /mnt/king && cp -r $1 /mnt/king && echo "cp2u success" && umount /mnt/king
}