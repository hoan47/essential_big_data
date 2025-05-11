#!/bin/bash

# Set up environment variables
INPUT_PATH="/user/hive/warehouse/work.db/job_benefit"
OUTPUT_PATH="/user/b2hhduser/benefit_popularity_output"

# Remove output directory if it exists
hdfs dfs -rm -r -f $OUTPUT_PATH

# Run the MapReduce job
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -files mapper.py,reducer.py \
    -mapper 'python3 mapper.py' \
    -reducer 'python3 reducer.py' \
    -input $INPUT_PATH \
    -output $OUTPUT_PATH

# Display the result
echo "Benefit Popularity Results:"
hdfs dfs -cat $OUTPUT_PATH/part-*