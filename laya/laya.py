# -*- coding: utf-8 -*-
from __future__ import print_function
import time

# picture
happy_text_1 = u"█  █  ████  ███  ████"
happy_text_2 = u"█ █   █  █   █   █  █"
happy_text_3 = u"██    ████   █   ████"
happy_text_4 = u"█ █   █  █   █    █ █  █"
happy_text_5 = u"█  █  █  █   █    █ █  █"
happy_text_6 = u" "
happy_text_7 = u" "
happy_text_8 = u"    ████"
happy_text_9 = u"    █  █"
happy_text_10 =u"    █"
happy_text_11 =u"    █  █"
happy_text_12 =u"    ████"
happy_text_13 =u" "
happy_text_14 =u" "
happy_text_15 =u" ███   █  █  ███  █   ██"
happy_text_16 =u" █ █   █  █  █    ██ ███"
happy_text_17 =u" █ █   ████  ███  █ █ ██"
happy_text_18 =u"█████  █  █  █    █   ██"
happy_text_19 =u"█   █  █  █  ███  █   ██"
happy_text_20 =u" "
happy_text_21 =u" "
happy_text_22 =u"████  ████  █ █ █   ███   ███  █  █  █  █  ████  █"
happy_text_23 =u"█  █  █  █  █████   █ █   █    █  █  █  █  █  █  █"
happy_text_24 =u"████  █  █   ███    █ █   ███  ████  █ ██  ████  █"
happy_text_25 =u"█     █  █  █████  █████  █    █  █  ██ █   █ █"
happy_text_26 =u"█     ████  █ █ █  █   █  ███  █  █  █  █   █ █  █"
happy_text_27 =u" "
happy_text_28 =u"Когда нибуть все у тебя будет хорошо, ну а пока, по традиции:"
happy_text_29 =u" "
happy_text_30 =u"____________________$$___________$$ "
happy_text_31 =u"_____________ _____$___$________$___$ "
happy_text_32 =u"__________________$_____$$$$$$_____ $ "
happy_text_33 =u"__________________$____***___***____$ "
happy_text_34 =u"________________ _$____$$_____$$____$ "
happy_text_35 =u"_________________$ _______$$$_______$ "
happy_text_36 =u"_____$$$$$$$$_____$________$_______$ "
happy_text_37 =u"_ __$$________$______$$_________$$ "
happy_text_38 =u"____$_________$_____$___$ $$$$$___$ "
happy_text_39 =u"_______$______$____$__$________$__$ "
happy_text_40 =u"_______$____ _$____$__$__________$__$ "
happy_text_41 =u"______$____$___$$$$__$__________$_ _$$$$ "
happy_text_42 =u"_____$___$____$____$__$________$___$___$ "
happy_text_43 =u"_____$__$__ ___$____$__$________$__$____$ "
happy_text_44 =u"____$___$______$____$__$____$ _$__$____$ "
happy_text_45 =u"______$__$______$____$___$_$_____$___$ "
happy_text_46 =u"_______$ ___$$$$$_$___$___$_$____$___$ "
happy_text_47 =u"__________$$$$$_$____$____$__ ___$____$ "
happy_text_48 =u"________________$$$_$_____$______$_$$$ "
happy_text_49 =u"______________________$$$$___$$$$$_____ "
happy_text_50 =u" "
happy_text_51 =u"Вот, тебе рисунок котика!"

#list of strings
kstr=[happy_text_1,happy_text_2,happy_text_3, 
happy_text_4, happy_text_5, happy_text_6, happy_text_7, happy_text_8,
happy_text_9, happy_text_10, happy_text_11,happy_text_12, happy_text_13, happy_text_14,
happy_text_15, happy_text_16, happy_text_17,happy_text_18, happy_text_19, happy_text_20,
happy_text_21, happy_text_22, happy_text_23,happy_text_24, happy_text_25, happy_text_26,
happy_text_27, happy_text_28, happy_text_29,happy_text_30, happy_text_31, happy_text_32,
happy_text_33, happy_text_34, happy_text_35,happy_text_36, happy_text_37, happy_text_38,
happy_text_39, happy_text_40, happy_text_41,happy_text_42, happy_text_43, happy_text_44,
happy_text_45, happy_text_46, happy_text_47,happy_text_48, happy_text_49, happy_text_50,
happy_text_51]

#output picture
for y in xrange(len(kstr)):
	for x in xrange(len(kstr[y])):
		if x < len(kstr[y])-1:
			print (kstr[y][x], end=""),
		else:
			print (kstr[y][x])
		sys.stdout.flush()
		time.sleep(0.05)

