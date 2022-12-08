# 위를 .bashrc에 적용하여 로그인시에 적용할 수 있다.
# .bashrc is not sourced when you log in using SSH. 
# You need to source it in your .bash_profile like this:
if [ -f ~/.bashrc ]; then
    # . ~/.bashrc
    echo "source ~/.bashrc" > ~/.bash_profile
fi