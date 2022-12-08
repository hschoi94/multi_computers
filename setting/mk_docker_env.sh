docker run -itd -rm --name $1 -v $INPUT:/input_data -v $WORKDIR:/workspace $CODE:/code $2
