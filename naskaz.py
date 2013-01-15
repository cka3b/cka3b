# naskaz.py #
import sys
import codecs
import ru2CKA3b

infile = codecs.open(sys.argv[1], mode="r", encoding='utf-8')
outfile = codecs.open(sys.argv[2], mode="w", encoding='utf-16')

for line in infile.readlines():
  line2= ru2CKA3b.convert(line)
	outfile.write(line2)

outfile.close()
