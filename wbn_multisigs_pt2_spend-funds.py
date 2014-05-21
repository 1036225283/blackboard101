# MULTISIGS - PART TWO - SPENDING FROM A 2-of-3 MULTISIG ADDRESS
# This simple wallet works with bitcoind and will only work with 2-of-3 multisigs
# wobine code for world bitcoin network blackboard 101
# Educational Purposes only
# Python 2.7.6 and relies on bitcoind & bitcoinrpc & wobine's github connection file
# We had to change the bitcoinrpc 'connection.py' file to add multisig support
# you'll need to download our 'connection.py' file from Github & stuff it in your bitcoinrpc folder

#import sys;
#sys.path.append("D:\github\python-bitcoinrpc\bitcoinrpc")

from bitcoinrpc.authproxy import AuthServiceProxy



bitcoin = AuthServiceProxy("http://test:123456@127.0.0.1:8332")#creates an object called 'bitcoin' that allows for bitcoind calls

SetTxFee = int(0.00005461*100000000) # Lets proper good etiquette & put something aside for our friends the miners

ChangeAddress = bitcoin.getnewaddress();

unspent = bitcoin.listunspent() # Query wallet.dat file for unspent funds to see if we have multisigs to spend from

print "���Ǯ������Щ��ַ�� ",len(unspent)," ����ַ���Ի���"
for i in range(0, len(unspent)):
    print
    print "�� ",i+1," ����ַ�� ",unspent[i]["amount"]," �����رң��൱�� ",int(unspent[i]["amount"]*100000000),"��"
    print "���Ĵ���ID ",i+1,"��"
    print unspent[i]["txid"]
    print "ScriptPubKey�� ", unspent[i]["scriptPubKey"]
    print "��ַ =====>>",unspent[i]["address"]

print
totalcoin = int(bitcoin.getbalance()*100000000)
print "Ǯ���ܶ��ǣ�", totalcoin, "��"
print

WhichTrans = int(raw_input('���뻨���ĸ���ַ�ϵı�? '))-1
if WhichTrans > len(unspent): #Basic idiot check. Clearly a real wallet would do more checks.
    print "��Ǹ�����ַ�����ڣ���ȷ������������" 
else:
    tempaddy = str(unspent[WhichTrans]["address"])
    print
    if int(tempaddy[0:1]) == 1:
        print "����һ����ͨ��ַ�����������ǩ����ַ�����"
    elif int(tempaddy[0:1]) == 3:
        print "��ַ��",tempaddy
        print "��3��ͷ�ĵ�ַ��ζ������һ������ǩ����ַ."
        print
        print "���Ͷ���ǩ����ַ�ϵıң���Ҫ���µ�һЩ����: txid, scriptPubKey,  redeemScript"
        print "��Щ���������listunspent��������"
        print
        print "txid :",unspent[WhichTrans]["txid"]
        print "ScriptPubKey :", unspent[WhichTrans]["scriptPubKey"]
        print
        print "redeemScript :",unspent[WhichTrans]["redeemScript"]
        print
        
        print "�������ַ���� ",int(unspent[WhichTrans]["amount"]*100000000)," ��"

        HowMuch = int(raw_input('����֧������ '))
        if HowMuch > int(unspent[WhichTrans]["amount"]*100000000):
            print "��Ǹ�˻���û����ô��Ǯ" # check to see if there are enough funds.
        else:
            print
            
            SendAddress = str(raw_input('���͵��ĸ���ַ�� (����33hxAeUqNnFs3gdayu7aAaijhTbbfnphq8) ')) 
            if SendAddress == "33hxAeUqNnFs3gdayu7aAaijhTbbfnphq8":
                print "̫��л�ˣ���ѡ�������johnson Diao"
            print
            Leftover = int(unspent[WhichTrans]["amount"]*100000000)-HowMuch-SetTxFee
            print "��Ҫ�������ı��رҵ������ַ��",SendAddress,"�˻���������� ", Leftover," ��","����Щ�һᷢ�͵������ַ��",ChangeAddress
            print "�ᷢ�� ",SetTxFee," �ϵ����������Ѹ���"
            print
            print "��Ҫ�������͵�"
            
            
            rawtransact = bitcoin.createrawtransaction ([{"txid":unspent[WhichTrans]["txid"],
                    "vout":unspent[WhichTrans]["vout"],
                    "scriptPubKey":unspent[WhichTrans]["scriptPubKey"],
                    "redeemScript":unspent[WhichTrans]["redeemScript"]}],{SendAddress:HowMuch/100000000.00,ChangeAddress:Leftover/100000000.00})
            print "���͵�Ϊ��", rawtransact
            print
            print
            print "��������Ҫ��˽Կ����ǩ��"
            multisigprivkeyone = str(raw_input("�������һ��˽Կ��"))
            print
            signedone = bitcoin.signrawtransaction (rawtransact,
                    [{"txid":unspent[WhichTrans]["txid"],
                    "vout":unspent[WhichTrans]["vout"],"scriptPubKey":unspent[WhichTrans]["scriptPubKey"],
                    "redeemScript":unspent[WhichTrans]["redeemScript"]}],
                    [multisigprivkeyone])
            print "ǩ�����"
            print signedone
            print
            print "��ʵ��Ӧ��ʱ�������԰���������ݷ����ڶ�����Կ�ĳ����ߣ�������ɵڶ���ǩ����������Ϣ����й¶����˽Կ����Ϊ"
            print "˽Կ�Ѿ������˼���"
            print
            multisigprivkeytwo = str(raw_input("������ڶ���˽Կ��"))
            print
            doublesignedrawtransaction = bitcoin.signrawtransaction (signedone["hex"],
                    [{"txid":unspent[WhichTrans]["txid"],
                    "vout":unspent[WhichTrans]["vout"],"scriptPubKey":unspent[WhichTrans]["scriptPubKey"],
                    "redeemScript":unspent[WhichTrans]["redeemScript"]}],
                    [multisigprivkeytwo])
            print "�ڶ���ǩ���Ľ����"
            print doublesignedrawtransaction
            print
            print "�������Ѿ�׼���÷���",HowMuch,"�ϵı��رҵ�",SendAddress
            print Leftover," �ϵı��رһᷢ�͵������ַ��",ChangeAddress
            print "������������ ",SetTxFee," ��"
            print

            ReallyNow = (raw_input('������ڵ���س������Ǯ���Ӷ��ص�ַ���ͳ�ȥ����ȷ����'))
            ReallyNow2 = (raw_input('��ģ�����Ĵ��㷢�����Ǯ�� '))
            print
            print "���������ǲ����Ǯ���ͳ�ȥ�ġ����ǿɲ�ϣ������Ϊ���нű��ܵ��κ���ʧ"
            print "���������뷢�����Ǯ�Ļ������Խ�������һ�綫�����Ƶ�bitcoin-qt������ڣ�Ȼ��س����Ҿ���ķ���ȥ��"
            print "sendrawtransaction "+"\""+str(doublesignedrawtransaction['hex'])+"\""

        
