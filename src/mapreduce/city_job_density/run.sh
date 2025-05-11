#!/bin/bash

# Set up environment variables
INPUT_CITY="/user/hive/warehouse/work.db/city"
INPUT_JOB_CITY="/user/hive/warehouse/work.db/job_city"
OUTPUT_PATH="/user/b2hhduser/city_job_density_output"

# Remove output directory if it exists
hdfs dfs -rm -r -f $OUTPUT_PATH

# Run the MapReduce job
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -files mapper.py,reducer.py \
    -mapper 'python3 mapper.py' \
    -reducer 'python3 reducer.py' \
    -input $INPUT_CITY,$INPUT_JOB_CITY \
    -output $OUTPUT_PATH

# Display the result
echo "Benefit Correlation Results:"
hdfs dfs -cat $OUTPUT_PATH/part-*