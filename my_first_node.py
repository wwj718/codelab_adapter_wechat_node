import itchat
from codelab_adapter_client import AdapterNode


class MyFirstNode(AdapterNode):
    def __init__(self):
        super().__init__()
        self.NODE_ID = "eim/extension_wechat" # 与 https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extensions_v3/extension_wechat.py 保持相同NODE_ID，以便于与 Scratch 中的 wechat 积木兼容。

    def send_to_scratch(self, content):
        message = self.message_template()
        message["payload"]["content"] = content
        self.publish(message)


my_first_node = MyFirstNode()


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    text = msg.text
    my_first_node.send_to_scratch(text)


try:
    itchat.auto_login(hotReload=True)
    itchat.run()
except KeyboardInterrupt:
    my_first_node.teminate()
