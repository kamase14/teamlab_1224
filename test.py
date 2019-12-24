import urllib.request as req
import urllib.error as err
import time
import itertools

def query(url):
	res = req.urlopen(url)
	return res.read()

token = "GgoqAQz5LwRodUwNqAehvcUvgtoSMO1v"


dict = [('ACCDC', 90), ('BACBD', 83), ('BBDCD', 83), ('DDBBA', 78), ('CDAAB', 77), ('ACCDA', 76), ('DAABC', 75), ('CBBDC', 74), ('CDCBB', 74), ('CCDDB', 73), ('AACBD', 72), ('BBBAD', 72), ('AABAC', 71), ('BABAA', 71), ('DACBC', 71), ('DBDAD', 70), ('BACAA', 69), ('AABCB', 68), ('CBBAB', 68), ('DDAAC', 68), ('ABBAA', 66), ('ACBDD', 66), ('AACCD', 65), ('ABABD', 65), ('ABDAC', 65), ('BDACB', 65), ('DCBCC', 65), ('DCBDA', 65), ('BBBAB', 64), ('ACCCB', 62), ('CCBDC', 62), ('ACCDD', 61), ('ADAAB', 61), ('ABBDB', 60), ('ABCDD', 60), ('BDDDC', 60), ('DAACC', 60), ('DCDBA', 60), ('BACAD', 59), ('BBBBC', 59), ('BBDCB', 59), ('CBADB', 59), ('ABACA', 58), ('ABADC', 58), ('ACDBB', 58), ('ADCDA', 58), ('CADDB', 58), ('CBCBD', 58), ('DAADA', 58), ('DBACA', 58), ('ABDDD', 57), ('BCAAC', 57), ('CDADA', 57), ('CDDAD', 57), ('DACBD', 57), ('DCDAD', 57), ('AABBA', 56), ('ADAAD', 56), ('BAACA', 56), ('BDADC', 56), ('ABDAD', 55), ('ACADB', 55), ('ACDAD', 55), ('ADCAC', 55), ('CACCD', 55), ('CCDAD', 55), ('DBCCD', 55), ('DDCBB', 55), ('ADAAC', 54), ('BAACC', 54), ('BBDAD', 54), ('BDADA', 54), ('CCDCC', 54), ('CDADD', 54), ('DAABD', 54), ('DAACD', 54), ('DAADC', 54), ('DACBB', 54), ('AACDD', 53), ('AADAD', 53), ('ABBDC', 53), ('ACBBC', 53), ('ADBBC', 53), ('BABAC', 53), ('BDAAD', 53), ('CCDCB', 53), ('DDCBD', 53), ('DDCDC', 53), ('DDDAA', 53), ('AACCB', 52), ('AACCC', 52), ('AACDA', 52), ('ACBCC', 52), ('ADCCC', 52), ('BBBAC', 52), ('BDCBB', 52), ('CACBB', 52), ('CDBBA', 52), ('DADAA', 52), ('DADBA', 52), ('DDDDA', 52), ('AABDA', 51), ('AACDB', 51), ('AADAA', 51), ('BABDA', 51), ('BBBDC', 51), ('BBDAC', 51), ('BCDBA', 51), ('BCDCD', 51), ('BDADD', 51), ('BDBBA', 51), ('CCCAD', 51), ('CDAAD', 51), ('DAADB', 51), ('DADDB', 51), ('AAAAD', 50), ('ABAAC', 50), ('ACADD', 50), ('ADCBB', 50), ('BBACA', 50), ('BCADC', 50), ('BCCDD', 50), ('BDAAB', 50), ('BDAAC', 50), ('BDDCC', 50), ('CABCB', 50), ('CACDA', 50), ('CBABD', 50), ('CCADB', 50), ('CCDDA', 50), ('CDCBD', 50), ('DCBBD', 50), ('ABABA', 49), ('ABCCD', 49), ('BAACD', 49), ('BACCD', 49), ('BCCBB', 49), ('CABCD', 49), ('CBBCA', 49), ('CDCBA', 49), ('DAABA', 49), ('DBBAD', 49), ('DBBDC', 49), ('DCBBA', 49), ('DDBBB', 49), ('DDBCB', 49), ('AABDB', 48), ('ABACB', 48), ('ACCDB', 48), ('ADCBD', 48), ('BAABD', 48), ('BACAB', 48), ('BACBB', 48), ('BACBC', 48), ('BDCAD', 48), ('CACBA', 48), ('CDADC', 48), ('DABCB', 48), ('DBBAC', 48), ('DBBBA', 48), ('DCCDC', 48), ('DCDBD', 48), ('DDBBD', 48), ('DDCBC', 48), ('ABAAB', 47), ('ABDAA', 47), ('ACBBD', 47), ('BBCCD', 47), ('BCABA', 47), ('BCABC', 47), ('BCCDC', 47), ('BCDAD', 47), ('BDCBD', 47), ('BDDBB', 47), ('CBDAD', 47), ('CCBCC', 47), ('CDAAC', 47), ('CDDBB', 47), ('DAABB', 47), ('DCDBB', 47), ('DDAAA', 47), ('AAADA', 46), ('AACAD', 46), ('ABCBD', 46), ('BBDAA', 46), ('BBDCA', 46), ('BBDCC', 46), ('BDACC', 46), ('BDBDA', 46), ('BDDDA', 46), ('CAADA', 46), ('CABBB', 46), ('CADCB', 46), ('CBBDA', 46), ('DAACA', 46), ('DADCA', 46), ('DDADA', 46), ('DDDAD', 46), ('ABBAD', 45), ('ABBCC', 45), ('ABCDB', 45), ('ADADD', 45), ('ADDCB', 45), ('BAADA', 45), ('BBABD', 45), ('BCACC', 45)

tmp = 'ACCDCABDACDAABCBBDCDBACAACCBDCBACBD'
tmp_max = 91

for i in dict:
    for j in dict:
        moge = tmp + j[0]
        print(moge)
        time.sleep(1)
        url    = "https://runner.team-lab.com/q?token=%s&str=%s" % (token, moge)
        result = query(url)
        print(int(result))
        if tmp_max <= int(result):
            max = j[0]
            tmp_max = int(result)
            print(int(tmp_max))
    tmp += max
    if len(tmp) > 50:
        break

moge = tmp

url    = "https://runner.team-lab.com/q?token=%s&str=%s" % (token, moge)
result = query(url)
print(result)
