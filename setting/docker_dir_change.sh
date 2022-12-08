echo $(docker info | grep "Docker Root Dir")
if test -f '/etc/docker/daemon.json'; then
	number=$(ls -l /etc/docker/ | grep daemon.tmp* | wc -l)
	echo $number
	cp /etc/docker/daemon.json /etc/docker/daemon.tmp$number
else
	touch /etc/docker/daemon.json
fi

systemctl stop docker
docker_path='/media/workspace/docker_dir'
if test -f $docker_path; then
	echo "dir exist"
else
	mkdir $docker_path
	touch /etc/docker/daemon.json
fi
echo '{
"graph":' '"'"$docker_path"'"
}' > /etc/docker/daemon.json
systemctl start docker
echo $(docker info | grep "Docker Root Dir")
