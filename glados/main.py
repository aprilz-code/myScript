# import os
#
# from glados import *
# from push_message import *
#
# if __name__ == "__main__":
#
#     # pushplus平台token
#     pushplus_token = os.environ['PUSHPLUS_TOKEN']
#     # server酱token
#     server_token = os.environ['SERVER_TOKEN']
#
#     glados_cookie = os.environ['GLADOS_COOKIE']
#
#     if glados_cookie is None or len(glados_cookie) <= 0 or glados_cookie == '':
#         print('The glados_cookie is none')
#         exit(0)
#
#     cookie_string = glados_cookie.split("&&")
#     checkin_codes = list()
#
#     account_checkin_message = []
#     checkin_message = []
#     # 遍历cookie执行签到，并返回签到状态码和签到信息
#     for idx, cookie in enumerate(cookie_string):
#         print(f"【Account_{idx + 1}】:")
#         checkin_code, account_checkin_message = glados(cookie)
#         checkin_codes.append(checkin_code)
#
#         # 存在账户签到信息，说明成功执行了签到
#         if account_checkin_message is not None and len(account_checkin_message) > 0:
#             checkin_message.append(f"【Account_{idx + 1}】:" + account_checkin_message + "\n")
#
#     # 所有账号签到完毕，判断是否有签到信息，如果有签到信息说明账号执行了签到
#     if checkin_message is not None and len(checkin_message) > 0:
#         try:
#             # 推送签到消息至pushplus平台
#             if pushplus_token is not None and len(pushplus_token) > 0:
#                 pushplus_message(pushplus_token, ''.join(checkin_message))
#             else:
#                 print('The pushplus_token is none')
#             #     推送至server酱
#             if server_token is not None and len(server_token) > 0:
#                 server_messgae(token=server_token, title='Glados checkIn status', message=''.join(checkin_message))
#             else:
#                 print('The server_token is none')
#         except Exception as e:
#             print('push message error', str(e))
#
#     assert -2 not in checkin_codes, "At least one account login fails."
#     assert checkin_codes.count(0) + checkin_codes.count(1) == len(checkin_codes), "Not all the accounts check in successfully."
