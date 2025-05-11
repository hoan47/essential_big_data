#!/bin/bash

# Restore
hdfs dfs -cp -f /backup/work_load.db_backup/* /user/hive/warehouse/work_load.db/