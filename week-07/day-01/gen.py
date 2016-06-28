def filegen(amount):
    content = ''
    for i in range(amount):
        if i < 10:
            filename = '0'+str(i)+'.js'
        else:
            filename = str(i)+'.js'
        content = open(filename, 'a')
        content.close()


filegen(46)
