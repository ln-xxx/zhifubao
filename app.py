import os

from alipay import AliPay, DCAliPay, ISVAliPay
from alipay.utils import AliPayConfig
import os
app_private_key_string = open(".\keys\keysapp_private_key").read()

alipay_public_key_string = open(".\keys/alipay_public_key").read()


# #
alipay = AliPay(
    appid="2016110400791021",
    app_notify_url=None,  # 默认回调url
    app_private_key_string=app_private_key_string,
    # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
    alipay_public_key_string=alipay_public_key_string,
    sign_type="RSA2", # RSA 或者 RSA2
    debug=True,  # 默认False
    config=AliPayConfig(timeout=15)  # 可选, 请求超时时间
)

order_string = alipay.api_alipay_trade_wap_pay(
        out_trade_no=1111,  # 订单编号
        total_amount=str(8000000/100.0),   # 总金额
        subject=u"爱家租房 %s" % 1111,  # 订单标题
        return_url="http://www.baidu.com",  # 返回的连接地址
        notify_url=None  # 可选, 不填则使用默认notify url
    )
pay_url = 'https://openapi.alipaydev.com/gateway.do?' + order_string
print(pay_url)

result = alipay.api_alipay_trade_pay(
    out_trade_no="222",
    scene="bar_code/wave_code",
    auth_code="auth_code",
    subject="subject",
    discountable_amount=10,
    total_amount=20,
    notify_url="https://example.com/notify" # 可选, 不填则使用默认notify url
)

if  result["code"] == "10000":
    print("Order is paid")