from django.conf.urls import url

from . import views



urlpatterns = [

    #商城首页
    url(r'^$',views.index, name='index'),
    #商城列表页
    url(r'^list$',views.list, name='list'),
    #商品详情页
    url(r'^minute/(?P<gid>[0-9]+)$',views.minute, name='minute'),

    #用户登录页
    url(r'^userlogin$',views.userlogin, name='userlogin'),
    url(r'^userdologin$', views.userdologin, name="userdologin"),
    url(r'^userlogout$', views.userlogout, name="userlogout"),


    #用户注册页
    url(r'^register$',views.register, name='register'),
    url(r'^doregister$', views.doregister, name="doregister"),

    #个人主页
    url(r'^myindex/(?P<uid>[0-9]+)$',views.myindex, name='myindex'),
    url(r'^useredit/(?P<uid>[0-9]+)$',views.useredit, name='useredit'),
    url(r'^doedit/(?P<uid>[0-9]+)$',views.doedit, name='doedit'),


    # ==================================购物车页面===========================================
    # 浏览购物车
    url(r'^shopcart$',views.shopcart, name='shopcart'),
    # 添加购物车
    url(r'^shopcartadd/(?P<sid>[0-9]+)$',views.shopcartadd, name='shopcartadd'),
    #删除购物车物品
    url(r'^shopcartdel/(?P<sid>[0-9]+)$',views.shopcartdel, name='shopcartdel'),
    #清空购物车
    url(r'^shopcartclear$',views.shopcartclear, name='shopcartclear'),
    #更改购物车物品选择
    url(r'^shopcartchange$',views.shopcartchange, name='shopcartchange'),


    #===================================订单页=======================================
    #结算商品
    url(r'^orderone$',views.orderone, name='orderone'),
    #确认订单
    url(r'^ordertwo$',views.ordertwo, name='ordertwo'),
    #再次决定订单
    url(r'^ordertrue$',views.ordertrue, name='ordertrue'),
    #浏览我的订单
    url(r'^orderlist$',views.orderlist, name='orderlist'),


]