#!/bin/bash

# Check if URL argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Extract URL from command line argument
url=$1

# Send a GET request to the URL and capture the response body
response_body=$(curl -s -o /dev/null -w "%{http_code}" "$url")
if [ "$response_body" -eq 200 ]; then
    curl -s "$url"
    echo ""
else
    exit 1
fi

