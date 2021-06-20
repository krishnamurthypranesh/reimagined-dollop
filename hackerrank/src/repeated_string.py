inp = [['abcac', 10], ['aba', 10], ['a', 1000000], ['gfcaaaecbg', 547602],
        ['epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq',
    549382313570],
    ['ojowrdcpavatfacuunxycyrmpbkvaxyrsgquwehhurnicgicmrpmgegftjszgvsgqavcrvdtsxlkxjpqtlnkjuyraknwxmnthfpt',
685118368975], ['ababa', 3]]

def repeatedString(s: str, n: int) -> int:
    count = 0
    factor = n // len(s)
    mod = n % len(s)

    for i in s:
        if i == 'a':
            count += 1

    count = int(count * round(factor, 0))

    for i in list(s[:mod]):
        if i == 'a':
            count += 1

    return count


print(list(map(lambda x: repeatedString(*x), inp)))

