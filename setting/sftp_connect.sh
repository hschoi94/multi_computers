#!/bin/bash
echo $PASSWORD |sshfs $USER@$SERVER_IP:/srv/$UUID_DISK/$REMOTE_PATH $CLIENT_PATH -o idmap=user,uid=1000,gid=1000,IdentityFile=/home/$USER/.ssh/id_rsa -o password_stdin
