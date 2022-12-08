ssh $USER@$IPADDRESS "sudo -S<<<'$PASSWORD' df -h"
#nvidia-smi --query | fgrep 'Product Name'
#wol -> ssh -> scp -> {incron->(scp-C, shutdown)}