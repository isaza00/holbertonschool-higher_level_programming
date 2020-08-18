#!/bin/bash
# solve the puzzle to get respond "you got me"
curl -s -X PUT -d "user_id=98" -L -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
