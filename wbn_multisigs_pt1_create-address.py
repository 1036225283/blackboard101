# MULTISIGS - PART ONE - GENERATING A MULTISIG ADDRESS & REDEEM SCRIPT
# wobine code for world bitcoin network blackboard 101
# Educational Purposes only
# Python 2.7.6 and relies on bitcoind & bitcoinrpc & wobine's github connection file
# We had to change the bitcoinrpc 'connection.py' file to add multisig support
# https://github.com/wobine/blackboard101/blob/master/wbn_multisigs_pt1_create-address.py


from bitcoinrpc.authproxy import AuthServiceProxy

bitcoin = AuthServiceProxy("http://test:123456@127.0.0.1:8332") #creates an object called 'bitcoin' that allows for bitcoind calls

pubkey = dict()


print "�����빫Կ����Կ����������[validate address]�����pubKey�ֶεõ�"
pubkey[0] = str(raw_input("�����������1�Ĺ�Կ��"))
pubkey[1] = str(raw_input("�����������2�Ĺ�Կ��"))
pubkey[2] = str(raw_input("�����������3�Ĺ�Կ��"))
n = int(raw_input("�����뼸��˽Կ���Խ�����"))
threeaddy = [pubkey[0],pubkey[1],pubkey[2]]
print "����ǩ����ַ�ǣ�"
multisigaddy = bitcoin.addmultisigaddress(n,threeaddy)
multiaddyandredeem = (bitcoin.createmultisig(n,threeaddy))
print len(multisigaddy),"chars - ", multisigaddy
print
print "redeemScript -", len(multiaddyandredeem["redeemScript"]), "chars -",multiaddyandredeem["redeemScript"]
print
print "���ڿ��԰������������������������Ժ󻨷�ʱ���������"




