import gzip
import shutil
with gzip.open('/home/llmmarathi/Pendse/data-00000-of-00019.arrow', 'rb') as fin:
    with open('/mnt/HDFS1/llm/llmmarathi/Pendse/glot500/g1.txt', 'wb') as fout:
        #for small files this also works
        # data = fin.read()
        # fout.write(data)

        #for large files best
        shutil.copyfileobj(fin, fout)
