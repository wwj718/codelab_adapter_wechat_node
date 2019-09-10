import itchat
from codelab_adapter_client import AdapterNode


class MyFirstNode(AdapterNode):
    def __init__(self):
        super().__init__()
        self.EXTENSION_ID = "eim/wechat"

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
