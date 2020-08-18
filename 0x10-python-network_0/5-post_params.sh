#!/bin/bash
#make a post request with email an subject as params
curl -s -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
