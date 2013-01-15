#  ru2CKA3b.py #
import codecs
import re
import RU
import CKA3b

# Check if the function already exists first
try:
  enumerate
except:	
# Allow access like a builtin function
	import __builtin__
	__builtin__.enumerate = lambda seq: zip(xrange(len(seq)), seq)

# map RU->skaz
mapRU2CK = {
	RU.Capital_Letter_Io : CKA3b.skzCAPITAL_IOTED_O,
	RU.Capital_Letter_A : CKA3b.skzCAPITAL_A,	
	RU.Capital_Letter_Be : CKA3b.skzCAPITAL_B,	
	RU.Capital_Letter_Ve : CKA3b.skzCAPITAL_V,	
	RU.Capital_Letter_Ghe : CKA3b.skzCAPITAL_G,	
	RU.Capital_Letter_De : CKA3b.skzCAPITAL_D,	
	RU.Capital_Letter_Ie : CKA3b.skzCAPITAL_IOTED_E,	
	RU.Capital_Letter_Zhe : CKA3b.skzCAPITAL_ZH,	
	RU.Capital_Letter_Ze : CKA3b.skzCAPITAL_Z,	
	RU.Capital_Letter_I : CKA3b.skzCAPITAL_I,	
	RU.Capital_Letter_Short_I : CKA3b.skzCAPITAL_CENTRAL_I,	
	RU.Capital_Letter_Ka : CKA3b.skzCAPITAL_K,	
	RU.Capital_Letter_El : CKA3b.skzCAPITAL_L,	
	RU.Capital_Letter_Em : CKA3b.skzCAPITAL_M,	
	RU.Capital_Letter_En : CKA3b.skzCAPITAL_N,	
	RU.Capital_Letter_O : CKA3b.skzCAPITAL_O,	
	RU.Capital_Letter_Pe : CKA3b.skzCAPITAL_P,	
	RU.Capital_Letter_Er : CKA3b.skzCAPITAL_R,	
	RU.Capital_Letter_Es : CKA3b.skzCAPITAL_S,	
	RU.Capital_Letter_Te : CKA3b.skzCAPITAL_T,	
	RU.Capital_Letter_U : CKA3b.skzCAPITAL_U,	
	RU.Capital_Letter_Ef : CKA3b.skzCAPITAL_F,	
	RU.Capital_Letter_Ha : CKA3b.skzCAPITAL_KH,	
	RU.Capital_Letter_Tse : CKA3b.skzCAPITAL_TS,	
	RU.Capital_Letter_Che : CKA3b.skzCAPITAL_TCH,	
	RU.Capital_Letter_Sha : CKA3b.skzCAPITAL_SH,	
	RU.Capital_Letter_Shcha : CKA3b.skzCAPITAL_SCH,	
	RU.Capital_Letter_E : CKA3b.skzCAPITAL_E,
	RU.Capital_Letter_Yu : CKA3b.skzCAPITAL_IOTED_U,	
	RU.Capital_Letter_Ya : CKA3b.skzCAPITAL_IOTED_A,	
	RU.Small_Letter_Io : CKA3b.skzIOTED_O,
	RU.Small_Letter_A	        : CKA3b.skzA,
	RU.Small_Letter_Be	        : CKA3b.skzB,	
	RU.Small_Letter_Ve	        : CKA3b.skzV,	
	RU.Small_Letter_Ghe	    : CKA3b.skzG,	
	RU.Small_Letter_De	        : CKA3b.skzD,	
	RU.Small_Letter_Ie	        : CKA3b.skzIOTED_E,	
	RU.Small_Letter_Zhe	    : CKA3b.skzZH,	
	RU.Small_Letter_Ze	        : CKA3b.skzZ,	
	RU.Small_Letter_I	        : CKA3b.skzI,	
	RU.Small_Letter_Short_I	 : CKA3b.skzCENTRAL_I,	
	RU.Small_Letter_Ka	        : CKA3b.skzK,	
	RU.Small_Letter_El	        : CKA3b.skzL,	
	RU.Small_Letter_Em	        : CKA3b.skzM,	
	RU.Small_Letter_En	        : CKA3b.skzN,	
	RU.Small_Letter_O	        : CKA3b.skzO,	
	RU.Small_Letter_Pe	        : CKA3b.skzP,	
	RU.Small_Letter_Er	        : CKA3b.skzR,	
	RU.Small_Letter_Es	        : CKA3b.skzS,	
	RU.Small_Letter_Te	        : CKA3b.skzT,	
	RU.Small_Letter_U	        : CKA3b.skzU,	
	RU.Small_Letter_Ef	        : CKA3b.skzF,	
	RU.Small_Letter_Ha        : CKA3b.skzKH,	
	RU.Small_Letter_Tse	 : CKA3b.skzTS,	
	RU.Small_Letter_Che	    	: CKA3b.skzTCH,	
	RU.Small_Letter_Sha	        : CKA3b.skzSH,	
	RU.Small_Letter_Shcha	    : CKA3b.skzSCH,	
	RU.Small_Letter_E	        : CKA3b.skzE,
	RU.Small_Letter_Yu	        : CKA3b.skzIOTED_U,	
	RU.Small_Letter_Ya          : CKA3b.skzIOTED_A
}

#convert function with softness parameter
def r2C(c, bSoftening):
	s = mapRU2CK[c]
	nS = ord(s)
	#nS = ( nS & ~CKA3b.bitmaskSOFT )
	nS = ( ord(mapRU2CK[c]) & ~CKA3b.bitmaskSOFT )
	if bSoftening:
		nS = nS | CKA3b.bitmaskSOFT
	return unichr(nS)

def convert(line):
	outline = u""
	for i, c in enumerate(line):
		if c in RU.CONSONANTS:
			if i < len(line):
				c2 = line[i+1]
				outline += r2C(c, c2 in RU.SOFTENING)
			else:
				outline += r2C(c, False)
		elif c in RU.WOVELS:
			if i > 0:
				c1 = line[i-1]
				outline += r2C(c, not (c1 in RU.CONSONANTS))
			else:
				outline += r2C(c, False)
		elif c in RU.SIGNS:
			#do nothing
			pass
		else:
			outline += c
	return outline
