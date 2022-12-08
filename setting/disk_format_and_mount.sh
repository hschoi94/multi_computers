#!/bin/bash
# use super user permission
# 문제가 있을 때 한번만 사용하는 것.
if [ $# -ne 2 ]; then
    echo "Usage: $0 disk path"
    echo "CHECK: sudo fdisk -l"
    exit -1
else
    echo "param ok" 
    $DISK = $1
    $PATH = $2
    echo "n p 1 enter, enter, p w"
    fdisk $DISK #파티션 생성할 장치의 파티션 생성
    mkfs.ext4 $DISK # 파티션 포맷
    mkdir -p $PATH #연결할 디렉토리 생성
    blkid | grep /dev/$DISK | tee -a /etc/fstab # blkid: UUID 확인
    # vi /etc/fstab 이 파일에 기입 UUID=$uuid /data ext4 defaults 0 0 자동으로 마운트 하게 해줌
    mount -a # mounting
    df -h #마운트 확인
fi