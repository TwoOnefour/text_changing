import random
import re
import json
import os


class ChangingText:
    def __init__(self):
        with open("texts.json", "r", encoding="utf-8") as f:
            self.texts = json.loads(f.read())

    def changing(self, text):
        pass

    def get_random(self):
        return str(random.randint(1, len(self.texts)))

    def run(self):
        text_index = self.get_random()
        for i in self.texts[text_index]:
            print(f"原句为：{self.texts[text_index][i]}")
            text = self.texts[text_index][i].replace(i, input(f"请输入替换{i}的名字:"))
            print(text)
            if self.clip_to_clipboard:
                os.system(f"echo {text} | clip")
                print("已复制到剪切板")


if __name__ == "__main__":
    test = ChangingText()
    test.clip_to_clipboard = True  # 复制到剪切板
    test.run()
