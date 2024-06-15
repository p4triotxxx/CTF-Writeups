from Crypto.Util.number import *

flag = bytes_to_long(open("flag.txt", "rb").read())
e = 0x10001
p, q, r = [getPrime(1024) for _ in "123"]
c = pow(flag, e, p * q * r)

# Now count to 3
one = p * q * r
two = p + q + r
three = p**3 + q**3 + r**3

print(f"{one = }")
print(f"{two = }")
print(f"{three = }")
print(f"{c = }")

'''
one = 2011992281550613662176607026304893084819096311919010975575593928096711804391648044648021069354614085681705570494716265309933745234732524601164406877991226438291226411498391148262872363010339221024801399028004515111025223956089686894839690520789231091535233213641439402967143569756935696430430908171131908258620815960000485310390599089499487010794710745562769940575975954413304275534660518691326147985333007825941624737902382037501516955343741816764430370564374371512685774534846491951964107765745164165492721606328844063062664207151794573394917819315450423241127659425735663931349366756599701297325579271233320576213335764538092244352141103776890913217143436727223835803140847973150830336017622853468331564425127326770713011363239100769089846648474844027762182949807416280441647697997996319526353474835952997656819650459738492042420012380995357255631242641259299728282537771067205556178586924952079887533722298922813349092527
two = 386712172608587905845812362559715815090909098339325058856227655816373760973278927124401153515132888820898312608112694187320459472588727975991315665715927044727551096425560386992659305891438141613409415271843249785968260471543265262665136264796540639688309711135946739120399687081948686162832826233340060835609
three = 7222963570179712692243323424004896468685557410292215982775140025467769202770073560419992206820592784737441163643628450768592461586782601816323505070293536217026263581391332255594084213849285639908272749801352540212347206720766700389458881785897242444885272315229087711778539179360813845158511898218678345495761209460435506248750156005769399293536556196870803011328518788027823693430496484271496881698465339118185963228402105815896299703784593564686992846131456279809978630343854204392485109937968390556703226982039358221504848806508641941088328653684027428793554892476051540726841112912838052571766778401207450070767467331633102263162834494170280970107153567300107158920130367749927658540685659841180926956176308750879059681143060953454481651465980048706392875768059844030967129194681517786250908203029236169624973144716845290658263683641397297224240074459104854712356335927394600600452159637407132775437515475572665674300681
c = 111616802760564138278714840001544308941025042621084079921231338299008610256545709372808285035191303673937679184956575685875655936478976312541651294987467781646298452740180443208558231472510823740798854541687022976152190000707242420818487244188579520854676423703243919940869516240580141480178227500387164361483716172018426059750030133574996497043961598136211502678041199836622289943189157586015148696375208951472434655051787492038149214725874273991310915638613674447198908744803531754849286302914318577605304844433494369598917646633098558099583198706702598276772258472415966658979504694029915419231422053073781163037443593039501280990433091263238990565794939057750847522684127512426059132292069748378195946208788742501300169985379681924006550656118415573357543775130483201719562386377889540401578878738543710386827269626647040282045889753441047349355649036540729603095290341370619380129962911397392327317170294487218016605031
'''