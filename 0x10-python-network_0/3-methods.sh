#!/bin/bash
#return methods allowed
curl -I -s "$1" | grep Allow | cut -d" " -f2-
