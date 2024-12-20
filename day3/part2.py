# https://adventofcode.com/2024/day/3
import re
from typing import List

from input_util import read_file_as_list


def solution(matrix: List[str]) -> int:
    return sum(map(multiply_and_sum, matrix))


def filter_commands(chunks: List[str]) -> List[str]:
    filtered = [chunks[0]]  # assume "do" by default
    print("VALID", filtered)
    for chunk in chunks[1:]:
        print("don't()", chunk)
        if "do()" in chunk:
            do_chunks = chunk.split("do()")
            print("VALID", do_chunks[1:])
            filtered.append("".join(do_chunks[1:]))
    print()
    return filtered


def multiply_and_sum(string: str) -> int:
    pattern = re.compile(r"mul\(([0-9]+), ?([0-9]+)\)")
    print(string)
    chunks = filter_commands(string.split("don't()"))
    print(chunks)
    return sum(int(match.group(1)) * int(match.group(2)) for match in pattern.finditer("".join(chunks)))


# print(solution(["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]))
print(solution(read_file_as_list("input.txt")))

print(solution(["%why();how()*-],+!mul(696,865)why()from()how():,;{where()mul(170,685)who()how()*from(881,957)?&select()mul(894,569):mul(648,114);[:from(657,891)how()mul(740,402)what()&/,do()~^why()who(762,850)mul(80,670)what()^mul(627,741),[?<'when()?-{/mul(609,307)mul(432,475)why()>/mul(325,720)how(555,834)-]~]who()from()mul(823,923)<mul(884,851)/?<;-#!*mul(696,404)[from()]from()%<mul(93,418) ?why()'mul(187,144):-/,where()'&mul(280,602)><##how()how()*mul(716,717)'[!:mul(694,196)mul(721,78),*mul(239,457)^who()%~who(),:mul(490,688)(select(140,964)~) where()mul(478,704)when()mul(707,387)?*from()[mul(867,836)how()from()%+?mul(574,230);select()&where()&(&!,mul(817,18)~@mul(995,936){:~#}[{what()how(933,435)%mul(698,758)-mul(155,15)^'who();{;when(538,128)what()([mul(987,654)/>@'mul(547,334)#who()who()mul(481,545)[select()}<*@what()@where()mul(297,163)>~;?mul(569,963) who()%;$?)mul(829,771)'^;<how()!mul(278,922):when()['+/mul(853,126)select()<#what()^where()^mul(592,699)@-when()@who()-from()]$what()mul(516,92)mul(595,56)select()[;who()#{mul(677,424)/how()where()select()*mul(372,577)why(151,413)&~<'how()when()why(576,783)mul(103,253),&#(&what()({<)mul(877,948)select()  what()when()mul(591,830)' mul(680,751)select()&~%when(342,703)-(do()mul(33,531)#mul(751,44)}!select(290,10)*why()where(926,27)mul(998,521)+ ;(when()mul(88,951)mul(138,676){ mul(124,751)<!mul(390,250) )?#%from()}who()+@mul(190,100)@*,~*what()]mul(875,335){~)?%;![,mul(798,35)*($!&where(421,181)mul(164,359)mul(243,559) &,-''+mul(946,934)]['mul(473,611)(mul(436,844)&don't()$'[:)*mul(323,105)(from()+<mul(403,154)mul(404,75)what(),:'<&from()-'when(951,634)don't()}<>^$$<}when()mul(551,298)-![>#%mul(269,961);;$%(select()don't()<where();(mul(986,541)^$#~what()':[<do() ?from()++,]mul(294,595)how()mul(140,343)&?when(645,695)select();who()mul(722,871),{when()from()%(]^@don't()@~](mul(892,4)[mul(27,39)$[from(880,299)<]mul(183,314)[how(275,880)-mul(377,858):who()*select()@-mul(214,884)#<mul(783,441)?!&mul(414,821),,mul(333,787){+-]+-$(*#do():@% where()-'why()?mul(239,3)mul(899,369)*-[>how()+(mul(490,391)why()where()}}]<])-mul(665,733)* ;select()% ;what()who()!mul(651,691)':mul(972,924)mul(898,314)'/when()><}$)select(196,43)when()mul(622,9)mul(790,299<]~>*from()mul(898,775)mul(433,345)?+mul(936,855)>who()@what()mul(110,344)%mul(375,719)?}'{&where(279,765)mul(846,455)^,{~#<{^;mul(266,935how())~:]-? who()mul(516,281)$~mul(443,485){(mul(798,807)%mul(289,360):*why()~{$!*?'do()?how()mul(316,376)*what()where()[mul(829,9)%$!what()$ &mul(140,439)[why() don't()where(451,986)%]from()mul(335,971),where()^,+mul(109,542);]-when()how()*~mul(209,405)who()$mul(132,427)when()#/>$]mul(773,709)]select()@<^mul(976,853)@where()mul(999,764)who()?^@mul(117,681)/{mul(940,729);})}mul(892,189)why()>,how() &mul(22,503)%+#mul(740,5)mul(848,467),where()>~#^[mul(827,812)!#?'what()$why()what()mul(365,268)$select()+mul(208,463)mul(676,938)"]))
print(24557233)
