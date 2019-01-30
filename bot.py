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

def receive_wx_text(msg):
	wxgroup.send('received:[{}] {}'.format(msg['sender'], msg['text']))


wxbot.join()