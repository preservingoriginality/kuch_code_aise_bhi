import pandas as pd
from fastparquet import ParquetFile
pf = ParquetFile('/home/llmmarathi/Pendse/data-00000-of-00019.parquet')
df = pf.to_pandas()
df.to_csv('/mnt/HDFS1/llm/llmmarathi/Pendse/glot500/g1.txt', index=False)
