#!/bin/bash
#make a get request with custom header equal to 98
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
