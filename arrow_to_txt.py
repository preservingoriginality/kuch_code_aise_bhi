import pyarrow as pa
import shutil
with pa.OSFile('/home/llmmarathi/Pendse/data-00005-of-00019.arrow', 'rb') as fin:
    with open('/mnt/HDFS1/llm/llmmarathi/Pendse/glot500/g6.txt', 'wb') as fout:
        #for small files
        # data = fin.read()     
        # fout.write(data)

        #for large files
        shutil.copyfileobj(fin, fout)
