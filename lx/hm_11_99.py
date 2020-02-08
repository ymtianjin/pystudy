def mu_table():
#     打印9行小星星
    #为嵌套循环，第一个while循环为在末尾打印行号。第二个while为打印小星星.row为行号，col为列号
    row = 1

    while row <= 9:
        col = 1
        while col <= row:
            print("%d * %d = %d" % (row, col , row*col), end="\t")
            col += 1
        print("")
        row += 1

mu_table()