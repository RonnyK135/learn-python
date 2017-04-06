#encoding: utf-8

'''
1.定义一个list存储数据
    users = []
    [(name,age,tel)]
2.while True:
3.让用户输入：input find/list/add/delete/update/exit
4.if
    add
        input(name)
        input(age)
        input(tel)
        检查用户是否存在，如果不存在则append users(name,age,tel)
                         提示用户已存在
    delete
        input(name)
        检查用户是否存在，如果不存在提示用户不存在
                         删除用户del pop remove
    update
        input(name)
        input(age)
        inpout(tel)
        检查用户名是否存在，如果不存在提示用户不存在
                           提示用户已经存在update [] = (name,age,tel)
                           两种方式，users[i] = ()或者先del，users.pop(user)
    find
        input(name)
        遍历users,比较名称是否相等
                    相等打印user信息
    list
        遍历users，打印user信息
    exit
        break
'''
users = []
user_info_tpl = '|{0:>20}|{1:>5}|{2:>20}|'
user_info_header = user_info_tpl.format('name','age','telephone')
while True:
    action = input('please input action(find/list/add/delete/update/exit):')
    if action == 'add':
        #增加用户
        name = input('请输入用户名：')
        age = input('请输入年龄：')
        tel = input('请输入电话号码：')
        is_exits = False
        for user in users:
            if name == user[0]:
                print('添加用户失败，原因是用户名已存在')
                is_exits = True
                break
        if not is_exits:
            users.append((name, age, tel))
            print('添加用户成功')
        print(users)
    elif action == 'delete':
        #删除用户
        name = input('请输入你要删除的用户名：')
        is_exits = False
        for user in users:
        #for i in range(len(users)):
            #if name == users[i][0]:
            if name == user[0]:
                is_exits = True
                print('删除用户成功')
                users.remove(user)
                #del users=[i]
                #users.pop(i)
                break
        if not is_exits:
            print('删除用户失败，原因是用户不存在')
        print(users)
    elif action == 'update':
        #更新用户
        name = input('请输入用户名：')
        age = input('请输入年龄：')
        tel = input('请输入电话号码：')
        is_exits = False
        for user in users:
            if name == user[0]:
                users.remove(user)
                is_exits = True
                break
        if is_exits:
            users.append((name,age,tel))
            print('更新用户成功')
            print(users)
        else:
            print('更新用户失败，错误原因是用户不存在')
    elif action == 'find':
        #查找用户
        name = input('请输入你要查找的用户名:')
        is_exits = False
        for user in users:
            if name == user[0]:
                print(user_info_header)
                print(user_info_tpl.format(user[0],user[1],user[2]))
                is_exits = True

        if not is_exits:
            print('没有该用户信息')

    elif action == 'list':
        #列出所有用户
        print(user_info_header)
        for user in users:
            print(user_info_tpl.format(user[0],user[1],user[2]))

    elif action == 'exit':
        #退出程序
        break
    else:
        print('输入错误')


