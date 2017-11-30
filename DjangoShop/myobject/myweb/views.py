from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import redirect

from django.core.urlresolvers import reverse

from myweb.models import Types,Goods,Orders,Detail

from myweb.models import Users

import time,math

#公共信息加载函数
def loadinfo():
    context={}
    context['type0list'] = Types.objects.filter(pid=0)
    return context


# 商城首页
def index(request):
    context= loadinfo()
    return render(request,"myweb/index.html",context)

# 商城商品列表页
def list(request):
    context = loadinfo()
    list = Goods.objects.filter()
    if request.GET.get('tid','') != '':
        list = list.filter()
    context['goodslist'] = list
    return render(request,"myweb/list.html",context)

# 商品详情页
def minute(request,gid):
    context = loadinfo()
    ob = Goods.objects.get(id=gid)
    #累加点击量
    ob.clicknum += 1
    ob.save()
    context['goods'] = ob
    return render(request,'myweb/minute.html',context)




# 会员登录表单
def userlogin(request):
    return render(request,'myweb/login.html')

# 会员执行登录
def userdologin(request):
    try:
        #根据账号获取登陆者信息
        user = Users.objects.get(username=request.POST['username'])
        print(request.POST['username'])
        print(user)
        #判断当前用户是否是可用用户
        if user.state == 1:
            #验证密码
            import hashlib
            m = hashlib.md5()
            m.update(bytes(request.POST['password'],encoding='utf8'))
            if user.password == m.hexdigest():
                print('-------------')
                #登录成功,将当前登录信息放入到session中,并跳转页面
                request.session['user'] = user.name
                request.session['zid'] = user.id
                request.session['address'] = user.address
                request.session['phone'] = user.username
                request.session['vipuser'] = user.toDict()
                print(request.session['vipuser'])
                print(request.session['vipuser']['id'])
                return redirect(reverse('index'))
            else:
                context = {'info':'登录密码错误'}
        else:
            context = {'info':'不是可用用户!'}
    except:
        context = {'info':'登录账号错误'}

    return render(request,'myweb/info.html',context)



# 会员退出
def userlogout(request):
    # 清除登录的session信息
    del request.session['user']
    # 跳转登录页面（url地址改变）
    return redirect(reverse('userlogin'))


# 会员注册表单
def register(request):
    return render(request,'myweb/register.html')

#用户注册页
def doregister(request):
    try:
        ob = Users()
        ob.username = request.POST['username']
        ob.name = request.POST['name']
        a = len(ob.username)
        if a == 11 and request.POST['password'] != '':
            # 获取密码并md5
            import hashlib
            m = hashlib.md5()
            m.update(bytes(request.POST['password'], encoding="utf8"))

            ob.password = m.hexdigest()
            ob.state = 1
            ob.save()
            context = {'info': '注册成功！'}
            print(context)
        else:
            return render(request,'myweb/register.html',context)
    except:
        context = {'info': '注册失败！'}

    return render(request, "myweb/info.html", context)

#个人主页
def myindex(request,uid):
    ob = Users.objects.get(id = uid)
    context = {'my':ob}
    return render(request,'myweb/myindex.html',context)

#打开编辑个人主页
def useredit(request,uid):
    try:
        ob = Users.objects.get(id=uid)
        context = {'my':ob}
        return render(request,"myweb/edit.html",context)
    except:
        context = {'info':'没有找到要修改的信息！'}
    return render(request,"myweb/info.html",context)

#执行编辑保存
def doedit(request,uid):
    try:
        print('------------------')
        print(request.POST['name'])
        
        ob = Users.objects.get(id=uid)
        ob.name = request.POST['name']
        ob.sex = request.POST['sex']
        ob.address = request.POST['address']
        ob.code = request.POST['code']
        ob.phone = request.POST['phone']
        ob.email = request.POST['email']
        ob.save()

        context = {'info':'修改成功！'}
    except:
        context = {'info':'修改失败！'}
    return render(request,"myweb/info.html",context)




#=====================================购物车======================================

#浏览购物车
def shopcart(request):
    context = loadinfo()
    if 'shoplist' not in request.session:
        request.session['shoplist']={}
    return render(request,'myweb/shopcart.html')


#添加购物车
def shopcartadd(request,sid):
    #获取要放入购物车中的商品信息
    goods = Goods.objects.get(id=sid)
    shop = goods.toDict();
    print(shop)
    #添加一个购买量的属性m
    shop['m'] = int(request.POST['m'])
    print(shop['m'])
    #从session中获取购物车的信息
    if 'shoplist' in request.session:
        shoplist = request.session['shoplist']
    else:
        shoplist = {}

    #判断此商品是否在购物车中
    if sid in shoplist:
        #商品数量加一
        shoplist[sid]['m']+=shop['m']
    else:
        #新商品添加进来
        shoplist[sid] = shop

    #将购物车信息放回到session
    request.session['shoplist'] = shoplist
    return redirect(reverse('shopcart'))
    # return render(request,'myweb/shopcart.html')


def shopcartdel(request,sid):
    shoplist = request.session['shoplist']
    del shoplist[sid]
    request.session['shoplist'] = shoplist
    return redirect(reverse('shopcart'))


def shopcartclear(request):
    context = loadinfo()
    request.session['shoplist'] = {}
    return render(request,'myweb/shopcart.html',context)


def shopcartchange(request):
    context = loadinfo()
    print(context)
    shoplist = request.session['shoplist']
    print(shoplist)
    #获取信息
    shopid = request.GET['gid']
    print('------------')
    print(shopid)
    post_num = int(request.GET['num'])
    print(post_num)
    if post_num<1:
        post_num = 1
    shoplist[shopid]['m'] = post_num #更改商品数量
    request.session['shoplist'] = shoplist
    return render(request,'myweb/shopcart.html',context)



#===============================订单部分====================================

def orderone(request):
    #获取要结账的商品的id
    ids = request.GET.get('gids','')
    if ids == '':
        return HttpResponse('请选择要结账的商品!')
    gids = ids.split(',')
    #获取购物车中的商品信息
    shoplist = request.session['shoplist']
    print(shoplist)
    #封装要结账的商品信息,以及累积总金额
    orderlist = {}
    total = 0
    for sid in gids:
        orderlist[sid] = shoplist[sid]
        #计算累计总金额
        total += shoplist[sid]['price']*shoplist[sid]['m']
    request.session['orderlist'] = orderlist
    print(orderlist)
    request.session['total'] = total

    return render(request,'myweb/orderone.html')

def ordertwo(request):
    xname = request.POST['name']
    print(xname)
    xphone = request.POST['phone']
    print(xphone)
    xaddress = request.POST['address']
    print(xaddress)
    
    if xname == '':
        request.session['xname'] = request.session['user']
    else:
        request.session['xname'] = xname
    if xphone == '':
        request.session['xphone'] = request.session['phone']
    else:
        request.session['xphone'] = xphone
    if xaddress == '':
        request.session['xaddress'] = request.session['address']
    else:
        request.session['xaddress'] = xaddress
    if xname == '' or xphone == '' or xaddress == '':
        return HttpResponse("信息不完善,无法完成订单!")
    return render(request,"myweb/ordertwo.html")

def ordertrue(request):
    #封装订单信息,并执行添加
    orders = Orders()
    orders.uid = request.session['zid']
    orders.address = request.session['xaddress']
    orders.linkman = request.session['xname']
    orders.phone = request.session['xphone']
    orders.addtime = time.time()
    orders.total = request.session['total']
    orders.status = 0
    orders.save()
    #获取订单详情
    orderlist = request.session['orderlist']
    shoplist = request.session['shoplist']
    #遍历购物信息,并添加订单信息详情
    for shop in orderlist.values():
        del shoplist[str(shop['id'])]
        detail = Detail()
        detail.orderid = orders.id
        detail.goodsid = shop['id']
        detail.name = shop['goods']
        detail.price = shop['price']
        detail.num = shop['m']
        detail.save()
    del request.session['orderlist']
    del request.session['total']
    request.session['shoplist'] = shoplist
    ZZ = '购买成功,订单号为:'+str(math.ceil(orders.addtime))+'SS'+str(orders.id)
    context = {'info': ZZ}
    return render(request,'./myweb/info.html', context)




#订单列表
def orderlist(request):
    context = loadinfo()
    #从session中获取登录者的id,并从订单orders中获取当前用户的所有订单
    orders = Orders.objects.filter(uid=request.session['zid'])
    #遍历当前用户的所有订单信息,并获取每个订单所对应的订单详情信息,并以detaillist属性放置
    for order in orders:
        #获取当前订单详情
        dlist = Detail.objects.filter(orderid = order.id)
        #将订单详情以detaillist属性放置到订单对象中
        order.detaillist = dlist
        #遍历当前订单详情,并追加每个商品的图片信息
        for detail in dlist:
            goods = Goods.objects.get(id = detail.goodsid)
            detail.picname = goods.picname
    context['orders'] = orders
    return render(request,"myweb/order.html",context)
    