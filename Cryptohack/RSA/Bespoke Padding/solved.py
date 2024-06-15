# from sage.all import *
# from Crypto.Util.number import *
# from pwn import *
# from json import *

# # https://en.wikipedia.org/wiki/Coppersmith%27s_attack#Franklin-Reiter_related-message_attack

# encrypted_flag = 7489715579918940746120358106844222881395950082924950987699572537738910723388283938964289918372134874471894014217794601879743511775308621698103646916078091575176522807642692002292804757494073519861604940440807368501780001624424736094807478071665613146571363688807380868223978112743268029927461032556050187892445932147698458405475454101109156053045705859297763894228075668503621594868042391110904248128174563680032635208268626758683993314990571566616037602917278111174474881179887890121406276869167920049679063381486226422814952758216916720420337971500344975092930048455090827539140275542512002029186959174090194261824
# modulus = 14948078452280406290076359112604934774120134483069394927109557351982170160687659368761253012320809680959760266779145289855264512693963802142199087148716754950618974699161421076060219348658622640301907031735842482945960624132248646683525367849295083885885570097964627154279294758921533712149980361779209841686589376638892946317911061916186892810427639078559983041841530587839582848697500687268645536653403857399003418522564883488006744296487701653958416447025188537597207251404866066446892281321813825184450677937207083827640585328787399886921636307570436951429753831346164359546114294444531863000823587303635867824683
# padding = [2734638335488818967327616692182071404532460971236596540552557515037064608830332683791482018844544108275465005968547288804148597253092689949653988108387581404658885531653274114289848582937001039457714972441678837585192925927323561745264377418881407712149121722944313993545346339289973867834119860183414609302951971924092285264499826324517406810563343999545667243630948318699247811274392485402316434157420002638920117383036104812272113401999376379396921688284050604473671097589938387225068121910768661882855036009677637395424268951736931621770231994822778063760567944560238934376950480000112907863050710577276291224270, 6395622846599349622013711627455668393812109066115972336377052869909234856738854266669788481326026199186125617032198910076637292040778990364235327450852820805832399375175325017104121818133348711483167570384734304733215450658413648948811055843978117873039398021034742849138023474636409579582111595086700787260475894649482530552420889664434261919899104881533391666521046860551725462876315240499985955942959284636556855630565302745090879610129375084972906930616177234929994040837226768945811403534376580215828821234306503579134978225103053921665261465656026272790924294820580774878264163898495398724702815036718687561450]

# def gcd(a,b):
#     while b:
#         a, b = b, a % b
#     return a.monic()

# P.<x> = PolynomialRing(Zmod(n))

# p1 = (padding[0][0] * x + padding[0][1]) ^ e - enc[0]
# p2 = (padding[1][0] * x + padding[1][1]) ^ e - enc[1]
# m = -gcd(p1, p2).coefficients()[0]
# flag = long_to_bytes(int(m)).decode()
# print(flag)

from Crypto.Util.number import *
from pwn import *
from json import *

e = 11

f = connect('socket.cryptohack.org', 13386)
f.recv()

f.sendline(dumps({'option': 'get_flag'}))
g1 = loads(f.recvuntil('\n'))

f.sendline(dumps({'option': 'get_flag'}))
g2 = loads(f.recvuntil('\n'))


enc_1 = g1["encrypted_flag"]
enc_2 = g2["encrypted_flag"]

a_1, b_1 = g1["padding"]
a_2, b_2 = g2["padding"]

n_1 = g1["modulus"]
n_2 = g2["modulus"]

assert n_1 == n_2
print("challenge has been Franklin-Reiter attack ")
print(a_1, a_2, b_1, b_2, enc_1, enc_2)

p.<x> = PolynomialRing(Zmod(n_1))

g1 = (a_1 * x + b_1) ** e - enc_1
g2 = (a_2 * x + b_2) ** e - enc_2

def gcd(a,b):
    while b:
        a, b = b, a % b
    return a.monic()

m = -gcd(g1, g2).coefficients()[0]
flag = long_to_bytes(int(m))

print(flag)