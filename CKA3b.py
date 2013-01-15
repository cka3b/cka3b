# CKA3b.py #
bitmaskSMALL = int("01", 2)
bitmaskSOFT = int("10", 2)

############################################
# Named characters
skzCAPITAL_I         = u'\uE028'  #  0b000101000
skzI                 = u'\uE029'  #  0b000101001
skzCAPITAL_IOTED_I   = u'\uE02A'  #  0b000101010
skzIOTED_I           = u'\uE02B'  #  0b000101011
skzCAPITAL_E         = u'\uE030'  #  0b000110000
skzE                 = u'\uE031'  #  0b000110001
skzCAPITAL_IOTED_E   = u'\uE032'  #  0b000110010
skzIOTED_E           = u'\uE033'  #  0b000110011
skzCAPITAL_CENTRAL_I = u'\uE048'  #  0b001001000
skzCENTRAL_I         = u'\uE049'  #  0b001001001
skzCAPITAL_A         = u'\uE058'  #  0b001011000
skzA                 = u'\uE059'  #  0b001011001
skzCAPITAL_IOTED_A   = u'\uE05A'  #  0b001011010
skzIOTED_A           = u'\uE05B'  #  0b001011011
skzCAPITAL_U         = u'\uE068'  #  0b001101000
skzU                 = u'\uE069'  #  0b001101001
skzCAPITAL_IOTED_U   = u'\uE06A'  #  0b001101010
skzIOTED_U           = u'\uE06B'  #  0b001101011
skzCAPITAL_O         = u'\uE070'  #  0b001110000
skzO                 = u'\uE071'  #  0b001110001
skzCAPITAL_IOTED_O   = u'\uE072'  #  0b001110010
skzIOTED_O           = u'\uE073'  #  0b001110011
skzCAPITAL_M         = u'\uE084'  #  0b010000100
skzM                 = u'\uE085'  #  0b010000101
skzCAPITAL_SOFT_M    = u'\uE086'  #  0b010000110
skzSOFT_M            = u'\uE087'  #  0b010000111
skzCAPITAL_N         = u'\uE0A4'  #  0b010100100
skzN                 = u'\uE0A5'  #  0b010100101
skzCAPITAL_SOFT_N    = u'\uE0A6'  #  0b010100110
skzSOFT_N            = u'\uE0A7'  #  0b010100111
skzCAPITAL_L         = u'\uE0B4'  #  0b010110100
skzL                 = u'\uE0B5'  #  0b010110101
skzCAPITAL_SOFT_L    = u'\uE0B6'  #  0b010110110
skzSOFT_L            = u'\uE0B7'  #  0b010110111
skzCAPITAL_R         = u'\uE0CC'  #  0b011001100
skzR                 = u'\uE0CD'  #  0b011001101
skzCAPITAL_SOFT_R    = u'\uE0CE'  #  0b011001110
skzSOFT_R            = u'\uE0CF'  #  0b011001111
skzCAPITAL_J         = u'\uE0F6'  #  0b011110110
skzJ                 = u'\uE0F7'  #  0b011110111
skzCAPITAL_P         = u'\uE180'  #  0b110000000
skzP                 = u'\uE181'  #  0b110000001
skzCAPITAL_SOFT_P    = u'\uE182'  #  0b110000010
skzSOFT_P            = u'\uE183'  #  0b110000011
skzCAPITAL_B         = u'\uE184'  #  0b110000100
skzB                 = u'\uE185'  #  0b110000101
skzCAPITAL_SOFT_B    = u'\uE186'  #  0b110000110
skzSOFT_B            = u'\uE187'  #  0b110000111
skzCAPITAL_F         = u'\uE188'  #  0b110001000
skzF                 = u'\uE189'  #  0b110001001
skzCAPITAL_SOFT_F    = u'\uE18A'  #  0b110001010
skzSOFT_F            = u'\uE18B'  #  0b110001011
skzCAPITAL_V         = u'\uE18C'  #  0b110001100
skzV                 = u'\uE18D'  #  0b110001101
skzCAPITAL_SOFT_V    = u'\uE18E'  #  0b110001110
skzSOFT_V            = u'\uE18F'  #  0b110001111
skzCAPITAL_T         = u'\uE1A0'  #  0b110100000
skzT                 = u'\uE1A1'  #  0b110100001
skzCAPITAL_SOFT_T    = u'\uE1A2'  #  0b110100010
skzSOFT_T            = u'\uE1A3'  #  0b110100011
skzCAPITAL_D         = u'\uE1A4'  #  0b110100100
skzD                 = u'\uE1A5'  #  0b110100101
skzCAPITAL_SOFT_D    = u'\uE1A6'  #  0b110100110
skzSOFT_D            = u'\uE1A7'  #  0b110100111
skzCAPITAL_S         = u'\uE1A8'  #  0b110101000
skzS                 = u'\uE1A9'  #  0b110101001
skzCAPITAL_SOFT_S    = u'\uE1AA'  #  0b110101010
skzSOFT_S            = u'\uE1AB'  #  0b110101011
skzCAPITAL_Z         = u'\uE1AC'  #  0b110101100
skzZ                 = u'\uE1AD'  #  0b110101101
skzCAPITAL_SOFT_Z    = u'\uE1AE'  #  0b110101110
skzSOFT_Z            = u'\uE1AF'  #  0b110101111
skzCAPITAL_TS        = u'\uE1C0'  #  0b111000000
skzTS                = u'\uE1C1'  #  0b111000001
skzCAPITAL_TCH       = u'\uE1C2'  #  0b111000010
skzTCH               = u'\uE1C3'  #  0b111000011
skzCAPITAL_DZ        = u'\uE1C4'  #  0b111000100
skzDZ                = u'\uE1C5'  #  0b111000101
skzCAPITAL_DZH       = u'\uE1C6'  #  0b111000110
skzDZH               = u'\uE1C7'  #  0b111000111
skzCAPITAL_SH        = u'\uE1C8'  #  0b111001000
skzSH                = u'\uE1C9'  #  0b111001001
skzCAPITAL_SCH       = u'\uE1CA'  #  0b111001010
skzSCH               = u'\uE1CB'  #  0b111001011
skzCAPITAL_ZH        = u'\uE1CC'  #  0b111001100
skzZH                = u'\uE1CD'  #  0b111001101
skzCAPITAL_SOFT_ZH   = u'\uE1CE'  #  0b111001110
skzSOFT_ZH           = u'\uE1CF'  #  0b111001111
skzCAPITAL_K         = u'\uE1E0'  #  0b111100000
skzK                 = u'\uE1E1'  #  0b111100001
skzCAPITAL_SOFT_K    = u'\uE1E2'  #  0b111100010
skzSOFT_K            = u'\uE1E3'  #  0b111100011
skzCAPITAL_G         = u'\uE1E4'  #  0b111100100
skzG                 = u'\uE1E5'  #  0b111100101
skzCAPITAL_SOFT_G    = u'\uE1E6'  #  0b111100110
skzSOFT_G            = u'\uE1E7'  #  0b111100111
skzCAPITAL_KH        = u'\uE1E8'  #  0b111101000
skzKH                = u'\uE1E9'  #  0b111101001
skzCAPITAL_SOFT_KH   = u'\uE1EA'  #  0b111101010
skzSOFT_KH           = u'\uE1EB'  #  0b111101011
skzCAPITAL_HA        = u'\uE1EC'  #  0b111101100
skzHA                = u'\uE1ED'  #  0b111101101
skzCAPITAL_SOFT_HA   = u'\uE1EE'  #  0b111101110
skzSOFT_HA           = u'\uE1EF'  #  0b111101111

abc_names = {
   skzCAPITAL_I        : "CAPITAL_I",
   skzI                : "I",
   skzCAPITAL_IOTED_I  : "CAPITAL_IOTED_I",
   skzIOTED_I          : "IOTED_I",
   skzCAPITAL_E        : "CAPITAL_E",
   skzE                : "E",
   skzCAPITAL_IOTED_E  : "CAPITAL_IOTED_E",
   skzIOTED_E          : "IOTED_E",
   skzCAPITAL_CENTRAL_I: "CAPITAL_CENTRAL_I",
   skzCENTRAL_I        : "CENTRAL_I",
   skzCAPITAL_A        : "CAPITAL_A",
   skzA                : "A",
   skzCAPITAL_IOTED_A  : "CAPITAL_IOTED_A",
   skzIOTED_A          : "IOTED_A",
   skzCAPITAL_U        : "CAPITAL_U",
   skzU                : "U",
   skzCAPITAL_IOTED_U  : "CAPITAL_IOTED_U",
   skzIOTED_U          : "IOTED_U",
   skzCAPITAL_O        : "CAPITAL_O",
   skzO                : "O",
   skzCAPITAL_IOTED_O  : "CAPITAL_IOTED_O",
   skzIOTED_O          : "IOTED_O",
   skzCAPITAL_M        : "CAPITAL_M",
   skzM                : "M",
   skzCAPITAL_SOFT_M   : "CAPITAL_SOFT_M",
   skzSOFT_M           : "SOFT_M",
   skzCAPITAL_N        : "CAPITAL_N",
   skzN                : "N",
   skzCAPITAL_SOFT_N   : "CAPITAL_SOFT_N",
   skzSOFT_N           : "SOFT_N",
   skzCAPITAL_L        : "CAPITAL_L",
   skzL                : "L",
   skzCAPITAL_SOFT_L   : "CAPITAL_SOFT_L",
   skzSOFT_L           : "SOFT_L",
   skzCAPITAL_R        : "CAPITAL_R",
   skzR                : "R",
   skzCAPITAL_SOFT_R   : "CAPITAL_SOFT_R",
   skzSOFT_R           : "SOFT_R",
   skzCAPITAL_J        : "CAPITAL_J",
   skzJ                : "J",
   skzCAPITAL_P        : "CAPITAL_P",
   skzP                : "P",
   skzCAPITAL_SOFT_P   : "CAPITAL_SOFT_P",
   skzSOFT_P           : "SOFT_P",
   skzCAPITAL_B        : "CAPITAL_B",
   skzB                : "B",
   skzCAPITAL_SOFT_B   : "CAPITAL_SOFT_B",
   skzSOFT_B           : "SOFT_B",
   skzCAPITAL_F        : "CAPITAL_F",
   skzF                : "F",
   skzCAPITAL_SOFT_F   : "CAPITAL_SOFT_F",
   skzSOFT_F           : "SOFT_F",
   skzCAPITAL_V        : "CAPITAL_V",
   skzV                : "V",
   skzCAPITAL_SOFT_V   : "CAPITAL_SOFT_V",
   skzSOFT_V           : "SOFT_V",
   skzCAPITAL_T        : "CAPITAL_T",
   skzT                : "T",
   skzCAPITAL_SOFT_T   : "CAPITAL_SOFT_T",
   skzSOFT_T           : "SOFT_T",
   skzCAPITAL_D        : "CAPITAL_D",
   skzD                : "D",
   skzCAPITAL_SOFT_D   : "CAPITAL_SOFT_D",
   skzSOFT_D           : "SOFT_D",
   skzCAPITAL_S        : "CAPITAL_S",
   skzS                : "S",
   skzCAPITAL_SOFT_S   : "CAPITAL_SOFT_S",
   skzSOFT_S           : "SOFT_S",
   skzCAPITAL_Z        : "CAPITAL_Z",
   skzZ                : "Z",
   skzCAPITAL_SOFT_Z   : "CAPITAL_SOFT_Z",
   skzSOFT_Z           : "SOFT_Z",
   skzCAPITAL_TS       : "CAPITAL_TS",
   skzTS               : "TS",
   skzCAPITAL_TCH      : "CAPITAL_TCH",
   skzTCH              : "TCH",
   skzCAPITAL_DZ       : "CAPITAL_DZ",
   skzDZ               : "DZ",
   skzCAPITAL_DZH      : "CAPITAL_DZH",
   skzDZH              : "DZH",
   skzCAPITAL_SH       : "CAPITAL_SH",
   skzSH               : "SH",
   skzCAPITAL_SCH      : "CAPITAL_SCH",
   skzSCH              : "SCH",
   skzCAPITAL_ZH       : "CAPITAL_ZH",
   skzZH               : "ZH",
   skzCAPITAL_SOFT_ZH  : "CAPITAL_SOFT_ZH",
   skzSOFT_ZH          : "SOFT_ZH",
   skzCAPITAL_K        : "CAPITAL_K",
   skzK                : "K",
   skzCAPITAL_SOFT_K   : "CAPITAL_SOFT_K",
   skzSOFT_K           : "SOFT_K",
   skzCAPITAL_G        : "CAPITAL_G",
   skzG                : "G",
   skzCAPITAL_SOFT_G   : "CAPITAL_SOFT_G",
   skzSOFT_G           : "SOFT_G",
   skzCAPITAL_KH       : "CAPITAL_KH",
   skzKH               : "KH",
   skzCAPITAL_SOFT_KH  : "CAPITAL_SOFT_KH",
   skzSOFT_KH          : "SOFT_KH",
   skzCAPITAL_HA       : "CAPITAL_HA",
   skzHA               : "HA",
   skzCAPITAL_SOFT_HA  : "CAPITAL_SOFT_HA",
   skzSOFT_HA          : "SOFT_HA"
}
