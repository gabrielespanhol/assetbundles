import dlt

@dlt.table
def tranformation():
  return spark.range(10)