#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url="$1"

size=$(curl -sI "$url" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r\n')

echo "$size"
