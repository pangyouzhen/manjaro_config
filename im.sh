path="/usr/share/idea/bin/idea.sh"
line=$(cat ${path} | grep -n Run | awk -F : '{print $1}')
val=`expr $line - 1`
echo "$val"
sed -i "${val}iexport GTK_IM_MODULE=fcitx" $path
sed -i "${val}iexport QT_IM_MODULE=fcitx" $path
sed -i "${val}iexport XMODIFIERS=@im=fcitx" $path