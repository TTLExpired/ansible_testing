#
# ~/.bashrc
#

# If not running interactively, don't do anything
# [[ $- != *i* ]] && return

# vim style
set -o vi

alias ls='ls --color=auto'
PS1='[\W]\$ '

# VIM
export EDITOR="vim"

# Make python3 default for my shell
alias python=python3
alias ipython=ipython3

# colored BASH
# PS1='\[\033[1;36m\]\u\[\033[1;31m\]@\[\033[1;32m\]\h:\[\033[1;35m\]\w\[\033[1;31m\]\$\[\033[0m\] '']]]]]]'

# export PYENV_ROOT="$HOME/.pyenv"
# export PATH="$PYENV_ROOT/bin:$PATH"
# eval "$(pyenv init -)"
# eval "$(pyenv virtualenv-init -)"
# pyenv virtualenvwrapper

PATH="/home/mossesb/perl5/bin${PATH:+:${PATH}}"; export PATH;
PERL5LIB="/home/mossesb/perl5/lib/perl5${PERL5LIB:+:${PERL5LIB}}"; export PERL5LIB;
PERL_LOCAL_LIB_ROOT="/home/mossesb/perl5${PERL_LOCAL_LIB_ROOT:+:${PERL_LOCAL_LIB_ROOT}}"; export PERL_LOCAL_LIB_ROOT;
PERL_MB_OPT="--install_base \"/home/mossesb/perl5\""; export PERL_MB_OPT;
PERL_MM_OPT="INSTALL_BASE=/home/mossesb/perl5"; export PERL_MM_OPT;

# Add path
export PATH=$PATH:/home/mossesb/.local/bin

# Add powerline
# if [ -f /usr/local/lib/python3.6/dist-packages/powerline/bindings/bash/powerline.sh ]; then
# source /usr/local/lib/python3.6/dist-packages/powerline/bindings/bash/powerline.sh
# fi
