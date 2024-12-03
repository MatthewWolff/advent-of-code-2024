# https://adventofcode.com/2024/day/3
import re
from typing import List

from input_util import read_file_as_list


def solution(matrix: List[str]) -> int:
    return sum(map(multiply_and_sum, matrix))


def multiply_and_sum(string: str) -> int:
    pattern = re.compile(r"mul\(([0-9]+), ?([0-9]+)\)")
    return sum(int(match.group(1)) * int(match.group(2)) for match in pattern.finditer(string))


print(solution(["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"]))
print(solution(read_file_as_list("input.txt")))
print(solution([
    "%why();how()*-],+!mul(696,865)why()from()how():,;{where()mul(170,685)who()how()*from(881,957)?&select()mul(894,569):mul(648,114);[:from(657,891)how()mul(740,402)what()&/,do()~^why()who(762,850)mul(80,670)what()^mul(627,741),[?<'when()?-{/mul(609,307)mul(432,475)why()>/mul(325,720)how(555,834)-]~]who()from()mul(823,923)<mul(884,851)/?<;-#!*mul(696,404)[from()]from()%<mul(93,418) ?why()'mul(187,144):-/,where()'&mul(280,602)><##how()how()*mul(716,717)'[!:mul(694,196)mul(721,78),*mul(239,457)^who()%~who(),:mul(490,688)(select(140,964)~) where()mul(478,704)when()mul(707,387)?*from()[mul(867,836)how()from()%+?mul(574,230);select()&where()&(&!,mul(817,18)~@mul(995,936){:~#}[{what()how(933,435)%mul(698,758)-mul(155,15)^'who();{;when(538,128)what()([mul(987,654)/>@'mul(547,334)#who()who()mul(481,545)[select()}<*@what()@where()mul(297,163)>~;?mul(569,963) who()%;$?)mul(829,771)'^;<how()!mul(278,922):when()['+/mul(853,126)select()<#what()^where()^mul(592,699)@-when()@who()-from()]$what()mul(516,92)mul(595,56)select()[;who()#{mul(677,424)/how()where()select()*mul(372,577)why(151,413)&~<'how()when()why(576,783)mul(103,253),&#(&what()({<)mul(877,948)select()  what()when()mul(591,830)' mul(680,751)select()&~%when(342,703)-(do()mul(33,531)#mul(751,44)}!select(290,10)*why()where(926,27)mul(998,521)+ ;(when()mul(88,951)mul(138,676){ mul(124,751)<!mul(390,250) )?#%from()}who()+@mul(190,100)@*,~*what()]mul(875,335){~)?%;![,mul(798,35)*($!&where(421,181)mul(164,359)mul(243,559) &,-''+mul(946,934)]['mul(473,611)(mul(436,844)&do() ?from()++,]mul(294,595)how()mul(140,343)&?when(645,695)select();who()mul(722,871),{when()from()%(]^@do():@% where()-'why()?mul(239,3)mul(899,369)*-[>how()+(mul(490,391)why()where()}}]<])-mul(665,733)* ;select()% ;what()who()!mul(651,691)':mul(972,924)mul(898,314)'/when()><}$)select(196,43)when()mul(622,9)mul(790,299<]~>*from()mul(898,775)mul(433,345)?+mul(936,855)>who()@what()mul(110,344)%mul(375,719)?}'{&where(279,765)mul(846,455)^,{~#<{^;mul(266,935how())~:]-? who()mul(516,281)$~mul(443,485){(mul(798,807)%mul(289,360):*why()~{$!*?'do()?how()mul(316,376)*what()where()[mul(829,9)%$!what()$ &mul(140,439)[why()"]))
print(solution([
    ";select()why()^mul(356,375)where()mul(644,829)select()+(&what()&]do()mul(371,455)#}when() select()$mul(652,219)how()/%; >#,'+mul(512,393)where()(+@do()!#where(387,495)select()} why(),where();mul(239,141)+where(){$<;*select()+,mul(96,709)#[how()* +mul(912,58)/,how()mul(683,735)$from()]mul(373,231)from()[why()*how()}%when()+mul(136,796){>do()#?@*mulselect(970,242)>mul(912,199)how()do(){),>:(#{@where()mul(210,692)!{when(386,55)? mul(930,193) '?mul(346,981)&+-mul(118,871)when()who())when(356,533)mul(953,458)[}why()[{<&<mul(456,691)/[)[select()),%from()who()mul(387,855)^}how()mul(836,825)[why()/mul(749,848)}>where()where()when()@&>where()mul(20,206)#when()select()from()why()$mul(900,802)~(;+(what()mul(995,20)$>'mul(652,338)>mul(363,197)', *?mul(574,101)(when()mul(49,923),;[@:)<mul(443,90),'when()do()~who()}/why(){ ,$?mul(530,543):from()%when(){mul(146,746)^/+]mul(228,661)/who()what()select()} select()mul(407,315)(?>$select()from()when()@mul(228,113)<from()when(455,516)&&do()when()!:who(100,513)what()-when()}mul(882,415)-why()~>where()'what()from(838,518)]what()do()@who()]~&mul(29,312)when()why()mul(510[^{*how(663,533)~[*&%mul(664,861)?;$*%+{/mulwho(),what()from()who()!,:where();mul(302,326)when()mul(83,497from()mul(35,835)[mul(429,210){#mul(481,597)+how()&++^+mul(945,205)%do()%*how()who()from()why(640,284) mul(373,756)'>from()when(904,81)}mul(377,402)mul(352,617)where()select(668,44)+$!mul(977,96)mul(925,147)% select()mul(757,594)mul(667,169) when()who()who()who()mul(12,935)where())%what()what()$from(964,723)mul(84,767)^from() @mul(137^mul(543,4)who()how()};>/do()+select()@}&:+}mul(604,839)from()when()~why()~what()}mul(351,200)where()<)what()}mul(433,87)/$ how()-}mul(666,797)#@+who()how()why()?from()mul(772,579),why()why()from()-{;-}mul(602,921)^>mul(471,330)what()};%when()';:*&mul(438,87)^{( where()!$*from()mul(130,21)from()-[mul(797,649)'{from()/when()mul(897,988) ;when()%!'mulwhy(596,766)$'?how()mul(582,139)} ^><;how(171,166)mul(893,362)where()-'from()how(),mul(371,80):'who(808,795)$mul(72,103)[mul(492,476)(when()~select()~[who()#why()mul(21,185),'?/mul(801,258))mul(548,942)"]))
print(solution([
    "?-$mul(975 &+#select(489,349)*who())who();)mul(124,21)#from()where()+)/*~ -mul(632,17)%$ do();%mul(123,308)mul(488,897)?>';$;where()/mul(249,145)>;select()select()}!]^?mul(204,865)$mul(80,588)-] ;(who()how()*mul(434,798)##)mul(44,74)-mul(520,141)/?(^>+/( who()mul(371,961)#who() ?mul(254,744)-who()*mul(499,955)how()from() >?mul(553,995)<mul(12;select()},;/!(]when()}mul(490,481)><when()&]mul(225,864)from()mul(262,958)~*;?*what();;do()select()%}mul(225,558)+how()>>)&-select()>mul(625,699)-,;mul(488,493)?mul(315,42)from()/,:$,,*when()mul(887,391)(#%{ mul(613,520)/'?where()<mul(608,359)@/how()@}mul(224,137:/]!?{#mul(766,604))}% {;!&[do()<'who())select()+:/>why()mul(709,981)~' how())[mul(460,872) when()%@/?mul(319,730)*) #mul(819,598):; #%mul(186,374)%+{mul(252,553)+}*;]:select()[how()mul(54,460)('mul(767,516)what()!&@[- /~-mul(420,721)where(167,817)}mul(393,198)/what()~^:from()'mul(776,849)<{:/ {?:what()select()mul(503,698)(>~when()what()[,mul(325,23)mul(650,340))mul(206,125)*<when(){~),#when():mul(663,717)!:from(311,319)~-^~from(300,345)mul(817,238) ~*]where()(]&&mul(666,75)( from()what()[^select()(!do()^when()>~%^[&how()<mul(16,177)#,mul(337,520)why(377,223)mul(243,60)^[mul(929,385)[;select()when()?/:?where()who()mul(144,182)<+(<@;select()#;mul(53,296)mul(430,787){mul(59,615)select()why(),mul(167,41)mul(679,808)who()?from(711,550)]?mul(60,619)select()!@why()!}do()@how(203,89)[mul(252,511)><;]/^when()%@(mul(793,635)-*~%how()how()where()<mul(611,932)+select()mul(50,375)]who(371,188)'why(990,8)mul(938,757);[from()how()mul(530,20)*what()<-):[*when()-mul(298,502)[%select()& (*from()how()mul(85,261)select()~>:mul(91,355)how()[mul(816,280)who(847,273)mul(456,335)%^}#+[mul(111,198)/^mul(104,459))when()%/]{[;why()!mul(915,477)$where()#>where()why()what()what()))mul(842,405)@^$who(){'mul(84,674){&} mul(146,155)mul(833,727);{/;@what()<when()select()^mul(224,512)how():~~%select()mul(624,262)^)^from()}*&mul(598,8))when(do()how()? ,why()'{where()mul(767,186)>mul(532,66)select()[<mul/[+*mul(220,744)~how()mul(92,404)(%+mul(36,189)from()do()mul(340,87)~select()select()where();)!}?mul(174,947)where(203,500)%:$mul(621!#?what()<+)* mul(52,254)why()?>'-]!who()what()'mul(415,148)~<-!{^mul(14,736)where()do()@who()%@>'<?%,mul(601,388)+[mul(128,458)who();;where()+[)<]%mul(585,532)%$when()!;what():mul(515,714) {]mul(473,405)>mul(935,316)how()[<;where()@why()>)what()mul(476,701)?~select()': ^from(639,569);mul(797&+>(%];@};+#!/usr/bin/perl[*/>mul(36,243)"]))
print(solution([
    "/select()->)*how(386,454)from()mul(300,315)from()#!select()- @-<;mul(363,667)@!<*#*/(^mul(834,851)$ where()@mul(872{{#>$']&how()mul(198,844)'%&# )~;'mul(99,189)!why()when()select()where();mul(834,111)who()mul(679,451):mul(39,313)%{mul(173,934))';'mul(798,4)&?select()who()[select()-mul(311,962)mul(698,905);/{>)?select()where()?mul(803,359)}*'[when())('do()}what()@why()$^what()-?mulwhere()mul(143,508)do())<$&$'mul(717,939)where() ?mul~<mul(571,633)mul(240,325)why()/who(881,208)~select(),mul(493,499)-@/+why()(!mul(209,846)-do();:;+)how() mul(805,851)mul(176,123)when()!:who()mul(311,38) select()?)?@[>$ mul(726,673){}mul(78,339)mul@<:mul(119,156)[how()@from()!!$select()mul(828,590)mul(182,837)from()mul(683,176)mul(892{!% who()+!^!mul(403,141)}(}{&mul(324,188)%how()mul(97,443)do()how() [mul(292,615)mul(32,672)<(>)^?$##mul(552,878)mul(190~[select(31,208)how(488,878),mul(803,157)from()]how()&mul(126,470+(*&mul(684,992)when()^[mul(292,454)<}}& ]%# mul(628,183){where()why()!where()where(637,929)^+]do()<from()^from()>[mul(673,37)mul(26,197)why()^where()where()>who()when()[-mul(732,481)<why()''(?mul(739,60)mul(735 ~why(305,335)/&do()@?'where()mul(14,42)!{select(286,515)#why()mul(229,685)who(){&[mul(395,229)where(254,749)]where()~mul(180,611)-["]))
print(solution([
    "why()mul(894,702)*how()?-mul(931,273)[-/from()(; mul(334,459)mul(988,980)[<why()<mul(845,3)why(),where(57,517)how()where()]{,&mul(159,943),:~what()mul(788,895)mul(431,498)&({:when()?!&>}mul(316,411),where()mul(160,695)#from()who()!](^'!mul(72,797)^^how();where())mul(117,420)mul(222,643)what()+*&,^#-who();mul(582,187)^'(what()/mul(762,337)why()[)%:&^'mul(200,220)#<why(4,955)[how()?,:mul(421,283) :^select() !mul(830,148)?how()*!mul(345,995)+{:mul(189,815)'$:#],:why()mul(449,429)when()mul(862,683)'mul(654,799);mul(608,309)mul(844,424):>what()[~(mul(869,922)-~mul(174,220)[)#how()+when()>'mul(336,741){[^]+!{^]?mul(72,869)why()mul(968,607)([~!-[/how()%when()mul(315,514)/*<#/?mul(287,442)< ;)*:~?why()mul(932,398); mul(339,6)what()what()%'!$-mul(541,481)*:%mul(278,722) '/mul(221,745)when()?why()'how()&select()mul(863,756)why())?mul(853,974)'~#*when()mul[^},mul(426,383);mul(363,22)+mul(48,755)'[?!+,}select()+mul(450,379) from()where()@![-#mul(504,685)what()!({how()/where()select()select(75,232)(mul(57,262)select()(mul(101,248)$~what()select()who() /!mul(963,497)*where()!~%how()>where()%select(185,346)mul(656,42)@?)$-mul(685,559)how(){^how()from()):]+mul(20,248)'-do()~select();(-[mul(558,465)from()who()who()//)-mul(339,776)';}what()from(837,48)how()do(),~~/mul(269,856)mul(857,460)>%?]/mul(792,512)&},*#mul(744,858);+[#!)(%-?mul(330,415)do()where()mul(527,833):where()+>-!mul(223,83)#![ how()!/mul(549,333),mul(595,422)~mul(980,75)<%^<^~%$mul(403,977)who()![<~what()])/from()mul(862,856)#^&?select()>  &+mul^)<^-{when()~{%mul(245,795))who())mul(998,777):@%how()mul(855,136where()<(]@what()#:how()>!mul(385,193)~-what()^why(){mul(844,123)what()#)&?mul(268,192)~&;how()when()>([)mul(316,777)mul(517,887)>(+,what(){mul(488,952)^?- mul(910,954)!%%mul(489,386)mul(665,70)%~when(620,413)/-{%mul(359-?+where()select()~mul(280,485)select()^:mul(821,371)who()}, why()<?[}mul(798,25)"]))
print(solution([
    "{select(){+-]:&when()mul(745,698)!&}:<from()}mul(139,392)where()>{what(698,375)##^#?}mul(49,637)where()/+[^@)$?mul(60,27)-:>why()#;$do()what(),&@-mul(197,825)when(177,701)-[@^why()#mul(113,357)#}why()/mul(779,647)/why()%from()mul(475,558)@?}who()what()~#; @mul(449,48)why();)[]#,>mul(909,644)%~>do()-}why()?>when()''$#mul(356,845): mul(75,208)*'*mul(197,931)from()>)&#+]mul(773,636)why()where()^}where()mul(895,801)from()(/^who()}why()[~-do()+/<['{when()mul(643,615)<[??who()mul(55,297)(?(mul(685,900):)who()when()%what()( ,~mul(684,595)why()who()]<where(939,153)from()?from(696,279)^mul(67,792)+:%$what()/mul(743,464)%do()<how(597,533)@mul(744,439):when()when()where()when()^}mul(241,329)+!who()when()^(+$where()mul(468,885)mul(172,30)^^]:<mul(314,256)]mul(185,690)> $mul(447,332)mul(857,945)&mul(211,6)-]%&<?}why()when()when(351,438)mul(966,579)when(365,315)mul(801,792)when()how()%#mul(275,938) ,)%]{from()mul(508,757)mul(303,112))}when() - )/mul(586,61)-when()-why()-{mul(186,812)*,mul(737,699);:(do()<{ mul(286,334)(-;how()where()how();;mul(388,580)<select()[how(){+{#who()mul(235,709)who(267,722){when();select()mul(917,863);how())>>select()from()mul(120,119)?*&select()who()mul(375,829)why()+%from()why(),*}+mul(378,224)#mul(330,898)mul(551,592)why()>do()&what()@from()@select()&<mul(448,624)where()<who(), -*"]))
print(sum([24557233,
           15584188,
           18766894,
           9331349,
           21087553,
           12882998]))