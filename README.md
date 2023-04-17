# myScript
自用脚本库   目前自己都是用PushPlus推送，其他推送方式自测 
 
【青龙】拉取仓库命令：`ql repo https://github.com/liroBoy/MT_fuli.git`

## glados 

[使用教程](https://www.losey.top/archives/glados%E7%A7%91%E5%AD%A6%E5%B7%A5%E5%85%B7%E6%97%A0%E9%99%90%E7%BB%AD%E8%B4%B9)

`glados_check_in.py`

`main.py  备用`

支持[server酱](https://sct.ftqq.com/)
支持[pushplus](https://www.pushplus.plus/)
推送


注册GLaDOS(注册地址在 https://github.com/glados-network/GLaDOS 实时更新), 并输入邀请码:
`KJEOR-J7LL1-3U23P-H69CG` 激活,可领取免费使用天数，亲测youtube，Netflix无压力。


## 星空代理签到
 `xkdaili.py`

变量：  
xingkong    多个用&连接  

举个例子 xingkong= 账号1:密码1&账号2:密码2 ....  

##小米运动 支持邮箱和手机号
xiaomi.py

变量：    
PMODE	推送模式,server酱推送:wx 新server酱推送:server tg推送:tg  PushPlus推送:pp 关闭推送:off  

PKEY	推送key,详见PKEY参数解释  
MI_USER	账号,仅支持手机号  
MI_PWD	密码  
MI_STEP	步数:自定义随机范围: 18000-25000  

举个例子：
PMODE： 'server'  
PKEY: 'sdasdas12312'  
MI_USER: '+8617666112171&110@qq.com'  
MI_PWD：'密码a&密码b'  
MI_STEP：'10000-20000&18000-20000'  


PKEY参数解释	格式  
TG推送	token@userid  
Server酱推送	填写server酱的推送key  
~~企业微信推送	推送用户（可@all）-corpid-corpsecret-(agentid 空则为默认1000002)~~  
PushPlus推送	token  
关闭推送	off  


# 美团

变量：  
MT_TOKEN


# 顺丰速运

变量：  
sfsyUrl

# 阿里云盘

变量：  
ALI_REFRESH_TOKEN
> 注意是refretoken ,登录后F12在localitemstorage点击token即可看到

Faker.spy懂的自然懂
