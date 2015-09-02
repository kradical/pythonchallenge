# http://www.pythonchallenge.com/pc/def/map.html
# k -> m
# o -> q
# e -> g


def main():
    s = "map.html"
    intab = "abcdefghijklmnopqrstuvwxyz"
    outtab = "cdefghijklmnopqrstuvwxyzab"
    print(s.translate({ord(x): y for (x, y) in zip(intab, outtab)}))

if __name__ == '__main__':
    main()