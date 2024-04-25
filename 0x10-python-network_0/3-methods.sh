#!/bin/bash
# shows all HTTP methods of server
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
