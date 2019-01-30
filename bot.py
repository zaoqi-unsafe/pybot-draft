config = {}
config['WxGroup'] = 'The Language'

import wxpy
wxbot = wxpy.Bot()
wxgroup = wxbot.groups().search(config['WxGroup'])[0]
@wxbot.register(wxgroup, wxpy.TEXT)
def wxbot_receive_raw(rawmsg):
	msg = {}
	msg['sender'] = rawmsg.member
	msg['text'] = rawmsg.text
	receive_wx_text(msg)

from aiocqhttp import CQHttp

qqbot = CQHttp(access_token='',
             enable_http_post=False)

@qqbot.on_message()
async def qq_handle_msg(context):
    await qqbot.send(context, '你好呀，下面一条是你刚刚发的：')
    return {'reply': context['message']}

def receive_wx_text(msg):
	wxgroup.send('received:[{}] {}'.format(msg['sender'], msg['text']))

qqbot.run(host='127.0.0.1', port=8194)
wxbot.join()