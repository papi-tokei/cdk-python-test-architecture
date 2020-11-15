#!/bin/bash

for dir in `ls -d */`; do
    cd "${dir}"
    if [ -f ./requirements.txt ]; then
        docker run --rm -v $(pwd):/var/task amazon/aws-sam-cli-build-image-python3.8:latest \
        pip install -r requirements.txt -t python/lib/python3.8/site-packages/
    fi
    cd -
done
