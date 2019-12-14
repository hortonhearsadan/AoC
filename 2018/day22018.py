import time

test_string='''
abcdef
bababc
abbcde
abcccd
aabcdd
abcdee
ababab
'''

string='''ymdrcyapvwfloiuktanxzjsieb
ymdrwhgznwfloiuktanxzjsqeb
ymdrchguvwfloiuktanxmjsleb
pmdrchgmvwfdoiuktanxzjsqeb
ymdrfegpvwfloiukjanxzjsqeb
ymdrchgpvwfloiukmanazjsdeb
ymdsnhgpvwflciuktanxzjsqeb
lmdrbhrpvwfloiuktanxzjsqeb
ymdrwhgpvwfloiukeanxzjsjeb
ymdrchgpvpfloihktanszjsqeb
omdrchgpvwflokuktanazjsqeb
kmsrchgpvwfloiuktanxqjsqeb
ymdrchopvwzloiustanxzjsqeb
omdrchgpvwfloiuktawxtjsqeb
ymdrchgpvwfroiukhanozjsqeb
ymdrchgpvwfloikktanyzosqeb
ymdrchgpvwfioiuktaexzjsqea
ymdrcngpvwfloiuktanxzjsamb
ymdrchgpqwfaoiuktanxxjsqeb
ymdrcmgpvwflziuktakxzjsqeb
ymdrchguvwsloiuktanxzjsqen
ymdrchppowfloiuvtanxzjsqeb
ymdrcngpvwflyiukkanxzjsqeb
ymdrcbgpvwfloiukjanxzjspeb
ymdrchgpvwflopuktanxzosseb
ygdrchgpvwfloiukxanxcjsqeb
ymdrchgpvwfloauktanuzjsqei
ymerchgpvwfloiumtanxzjsqet
ymdlcegpvwfloiuktbnxzjsqeb
ymdrclgpvwfloiukyanxzjlqeb
ymdrchgpvwhmoiuktanxijsqeb
ymdrchgpwrfloiuktanxdjsqeb
ymdbcwgpvwfloiuktanxzusqeb
ymgrchgphwfloiuktanxzjspeb
imdrchgpvwflmiuktanxzjsqib
ymdrihgpvwfloiiktanxzjsteb
ywdrchgpvwfloibkvanxzjsqeb
ymdrchgpxwfloiuktanezjsqes
ymdrchgpiwfloiukxanxzhsqeb
ymdrchgpveflokuktdnxzjsqeb
kmdrchgpvwfloviktanxzjsqeb
ymdrchgpvgfmoiuytanxzjsqeb
ymyrchgpvzfluiuktanxzjsqeb
ymdrchguvwfloiuktanxpjsqlb
ymerchgpvwfloiukthnxsjsqeb
hmdrchgpvwglfiuktanxzjsqeb
ymdrchgpvwfdoiuktanxzjsqaf
yudrchgdvwfloiuktaexzjsqeb
ymdbchgxvwfloiuktanxzjsqem
ymdrchgpvwfloiumjanxzjsqpb
ymdrchgpqwfloiuqtanxrjsqeb
ymdqchhpvwfloiuktanxzzsqeb
ymdryhgpfwfloiuktanxzjsyeb
xmdrchgpvwfloioitanxzjsqeb
ykdrchgpvwfloiuktcnxzisqeb
ymdrcpgprwfloiuktanqzjsqeb
yidrchgpvwfloiuktanxzjgleb
ymdrchgpxwfloiuktanxzjsxfb
ymdrchgfvwfloiuktanxzjiteb
ymdrchgvvwflqifktanxzjsqeb
ymdrchgplwfloiuktanizjnqeb
ymdrchgpvwfyfiuktafxzjsqeb
ymddchgpvwcloiuktanxzjsqeq
ymdrchgkvwflaiuktanxzjsqfb
yudrchgpvwfzoiuktanxzjsreb
ymdrdhgpvwfloiuktnnxqjsqeb
ymdrnhgpvwfloiuktauxzjdqeb
ymdrchgpvwflsiddtanxzjsqeb
ymdrchgpvwhloeuktanxzjsqek
ymdrchgpvjfioiuktawxzjsqeb
ycdrohgpvwfgoiuktanxzjsqeb
ymdrchgpvwflmifktanxzjsqel
yfdrchrpvwfloruktanxzjsqeb
ymdrchgjvwfloiuktanxzrsqeg
ymarchgpxwfloiukkanxzjsqeb
ymdrchgppwflghuktanxzjsqeb
ymdrchvpvwfloiuktanxpjrqeb
ymdlchgpqjfloiuktanxzjsqeb
ymdrchgpvwfofiuktandzjsqeb
ymdrcngpqwfloiuktanlzjsqeb
ymdrchgpvwfloiuiocnxzjsqeb
ymdrcogpvwfloizktanxzjcqeb
ymdrchgpvlfvoiuksanxzjsqeb
ymdrchgpvwflocpctanxzjsqeb
ymdrchgpvwfloiuktanlzjsejb
yndrchgpvwflzifktanxzjsqeb
ymdrcrgpvkfloiuktanxrjsqeb
ymdrchhpvwslocuktanxzjsqeb
ymdrxhgpvwfloiuwtazxzjsqeb
ymdrchgpvafloiuutanxzjsqxb
ymdrchppvhfloquktanxzjsqeb
ymprcugpvwtloiuktanxzjsqeb
ymdrchgpvvflyiuktanxzjsqvb
ymdrchgovwfloiuftanxzjwqeb
ymdrchrpvwflotyktanxzjsqeb
gmdrchgpvwfloauttanxzjsqeb
ymdrchmpvofloiukmanxzjsqeb
ymdrchgpvwflsiuktanxzjspkb
ymdrchgpvwfloluktajxijsqmb
ymdrcngpvwfloiukbanxzdsqeb
ymdrchgpvwploiuktnnxzmsqeb
ymdrcwgpvwfloiuktbnxhjsqeb
ymdrcngpvwfloiuktaaxbjsqeb
ykdrchgpvwfloiuktanxzgsqej
yuhrchgpvwfdoiuktanxzjsqeb
ymdrchgpvsfloiukbanxujsqeb
ymqrchgpvwfliiuktanxzjsteb
ysdqchgpvwfloiuktanxzjtqeb
ymdjchgpcwfloiuktanxzrsqeb
ymdkchgpvwfloiukfanlzjsqeb
ymdrchgpvxfloikktanxzjiqeb
smdrchgwewfloiuktanxzjsqeb
ymdrchgpvwfljiuktanxajsqer
ymdrchgpowflifuktanxzjsqeb
ymdrchgpvpzloiukoanxzjsqeb
yydrchgwvwfvoiuktanxzjsqeb
ymdgcdgpvwflobuktanxzjsqeb
ymdechgpvkfloiuktanxzjsjeb
ymdnchnpvwfloixktanxzjsqeb
ymdrchgpiefloiuktqnxzjsqeb
ymprchgpvwfloiuktjnxzjsxeb
ymdrjdgpzwfloiuktanxzjsqeb
ymsrchgpywfloiuktanxzjsueb
ymdrchgpvgoloiuktanxzcsqeb
ymdrphgpswflbiuktanxzjsqeb
ymqrchgpvnfloiumtanxzjsqeb
ymjrchgpvwyloiuktacxzjsqeb
ymdrchepvwmlqiuktanxzjsqeb
kmirchgpvwfloiuktanxzjsreb
ymdncygpvwfloiuktanuzjsqeb
ymdrzhgpvwploiuktanxzxsqeb
ymdrchkpvwfloiwkmanxzjsqeb
ywdrchgovwfloiuktanxzjsceb
amdrchgpvwfloiuktanrzjqqeb
ymdpshgpvwfloiuktanxzjyqeb
ymdrcegpvwfloijktcnxzjsqeb
ymdrcygpvwfloiuktanxztsqwb
ymdrchgpvufloiuvtabxzjsqeb
ymdrchgpvwflkiuktrnxzjsqmb
ymdrchgpvqfloiuktanxpjfqeb
ymdrclgpvkfloiyktanxzjsqeb
ybdxchgpvwfloiuktanxzjskeb
pmdrchgpvwfzoirktanxzjsqeb
ycdfchgpvwfloiuktanxzjtqeb
ymdrchgpdwfloiumtbnxzjsqeb
ymdrchgpqmfloiuktanxzjsqer
ymgrchgpvwfroiuktanxzjsqey
ymdrnhgpvwfloiuktanjzjsqlb
dmdrchgpvgfloiuktqnxzjsqeb
yudrchgnvwfloiukranxzjsqeb
ymdrxhgpvafloiuktanxzjsqeq
ymdrchgpvwfyofuktanxzjsueb
ymdrrhgpvwfloiuktavxzjsqpb
yvdrchgpvwfloiuktalxzhsqeb
ymdrchgpbwfloiuktanxzfnqeb
ymdrqhgpvwfloiuvtznxzjsqeb
ymdrchgpvbfloiuetanxzjsqeo
ymdrchjpvwfloiuktanxzjnqrb
ymdrchgpmwfqoiuknanxzjsqeb
ymdrchgpvwfuoiuktaqxzjtqeb
ymdrchgpvwfloiuktamxaosqeb
fmdrchgpvffloiuktanxzjsaeb
ymdrrhglvwfwoiuktanxzjsqeb
ymdrchgpvwflohuktanxzjcqei
ymdrcsgpvwfloiuktaexzjsqek
ymlrchfpvwfloiuktpnxzjsqeb
yxdrchgpvwfdoiuvtanxzjsqeb
ymdrchgrvwfloiuktadxzjsqew
ymdrchgpvwbloiyktandzjsqeb
ymdrchgpvsfloiyktanozjsqeb
ymdrchgpjwfloiuktanxibsqeb
ymdrchgjvyfloiuktanxzjsqeh
ymdrchgvvwfloiuktanzrjsqeb
ymdrchgpvwaloiuktynxzjsqev
ymdrccgpvwflonvktanxzjsqeb
ymdrchgqvffloiuktanxfjsqeb
ymdbchgpvwsloiudtanxzjsqeb
ymdachgpvwfloiuktanlzjsqwb
ymdrclgpvwwloiuktanxzjsjeb
ybdpchgpvwdloiuktanxzjsqeb
ymdtchgpvwfleijktanxzjsqeb
ymdrchgpvwfloiustanxzjsxep
ymdrcjypvwfloiuktanxnjsqeb
ymdrcdgpvwfloiuutanxkjsqeb
yhirchgpvufloiuktanxzjsqeb
ymdrlhgpvwfluigktanxzjsqeb
ywdrhhgpvwftoiuktanxzjsqeb
ymdrchgpvwflyiuktanozjsqtb
cmdrchgpuwfloiukmanxzjsqeb
ymdochgpvrfloiuktanvzjsqeb
ymdrcvgpvwfgoiuktfnxzjsqeb
ymdrchgpmufloiuktanxzssqeb
ymurchgrvwfloiuktanxzjsqep
bmdrchgpvwfloiukpanxzjsqmb
ymdrchgphwvloiuktanszjsqeb
ymdpkhgpvwfloiuktanxzjsqtb
ymdrchgpvwfloiuwtanxzjfqev
ymdrchgpvwfloguktqlxzjsqeb
ymkrshgpvwflgiuktanxzjsqeb
ymdrchgpzwfloizktanxznsqeb
ymdrchgpvxfloiuktegxzjsqeb
yydrchgpwwfloiuktanxzjsqqb
ymdrcngwvwfltiuktanxzjsqeb
ymdszhgwvwfloiuktanxzjsqeb
ymdrchguvwfjoiuktanxzxsqeb
ymdomhgpvwfloiuktanxgjsqeb
ymdrcvgpvwfloiuktanwzzsqeb
yydrchgpvwfloiuktanxzjmqtb
rmdrchgpvwfloiuktmnszjsqeb
ykdrchgpvwfloyuktmnxzjsqeb
ymcrchkpvwfloiuktanxzjsoeb
ymdrcrgpvwfloiukpanxzjsceb
yrdrchgpvwfloiukwanxzjsqhb
ymdrcfgpvwfloiurtanxojsqeb
ymdrchgpuwstoiuktanxzjsqeb
ymdrchgpvwflpxuktanxzjsqer
ymdrehgpvwfloiuktabxdjsqeb
yedrchgpvwfloiukqanxzjiqeb
ymdrthgpvyfloiuktanxzjsqen
cmdlchgpvwfloiuvtanxzjsqeb
ymdrchgpvwtloiuktanlpjsqeb
ymdrchgpvwfloiuktanyvjsqea
gmdrcogpvwfloiuktanxzjsqqb
ymmrchgpvwflosuktauxzjsqeb
ymgrchgjvwfloiuktavxzjsqeb
ymdbclgpvwfloeuktanxzjsqeb
ymdrchgpvwfloiuktaixzcsqfb
ymdrchgpvwflmiuktanxttsqeb
ymxrchgpvwfloiuktanxzfsqec
yqzrchgpcwfloiuktanxzjsqeb
yvdrchgpvwfloiukgvnxzjsqeb
ymdrchepvwfloiuktahxzosqeb
ymdlchgpvwfloiuktamizjsqeb
ymdrchgpcwflovuktanxzjsqzb
yvduchgpvwfloiukaanxzjsqeb
ymdrchgpvwfloiuktxmxzjsgeb
ymdrcrgpvwfloizktanbzjsqeb
amdrchgpvwfloiukhanxzjsqbb
ymdrchgpvwfloluktajxijsqeb
ymdrcfgpvwfloiubtanxznsqeb
ymdrchgpvwfleiuwtanxzjsweb
ymdrchgpvwfzdguktanxzjsqeb
ymdrchgwvwflosyktanxzjsqeb
ymrrchgpvwfloiultanxzjsqez
ymdpchgkvwfleiuktanxzjsqeb
ymdrchgpvwfloijktalxfjsqeb
ymdrchgpmwfloiuktanzzjsqfb
ymdrcsgpvwfljiukyanxzjsqeb
ymdrcarpvwfloiuktapxzjsqeb
ymdrchgpvwfloiuktanxzjcqvs'''

test_string2='''abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz'''



def run1():
    s = string.split('\n')
    twos=0
    threes=0
    for box_id in s:
        matched_2=False
        matched_3=False
        for unique in set(box_id):
            if box_id.count(unique) ==2 and not matched_2:
                twos+=1
                matched_2 = True
            if box_id.count(unique) == 3 and not matched_3:
                threes+=1
                matched_3 = True
            if matched_2 and matched_3:
                break
    return twos*threes


def run2():
    s = string.split('\n')
    t = s[:]
    num_matches = len(s[0])-1
    for i, box_id in enumerate(s):
        for j, box_id2 in enumerate(t):
            matches = [u for u, v in zip(list(box_id),list(box_id2)) if u ==v]
            if len(matches) ==num_matches:
                print(box_id2)
                print(box_id)
                return str().join(matches)




if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"2s*3s:", f)
    print(f"common letter in correct ids:", g)
