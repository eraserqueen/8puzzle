#!/usr/bin/env bash
export PYTHONPATH=$PYTHONPATH:`pwd`/src/main
python3 src/main/driver_3.py bfs 3,1,2,0,4,5,6,7,8
python3 src/main/driver_3.py bfs 1,2,5,3,4,0,6,7,8