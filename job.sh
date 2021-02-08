#!/bin/bash

WCDIR=/home/freq
STREAMINGJAR=share/hadoop/tools/lib/hadoop-streaming-2.7.0.jar

bin/hadoop jar $STREAMINGJAR                         \
    -files   $WCDIR/tfMap.py,$WCDIR/tfReduce.py      \
    -mapper  $WCDIR/tfMap.py                         \
    -reducer $WCDIR/tfReduce.py                      \
    -input   Gutenberg/'*'                           \
    -output  Gutenberg-out
