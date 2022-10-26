# wht
# 2022/10/10 16:48


class Expert:
    def __init__(self, num, name, title):
        self.num = num
        self.name = name
        if ("教授" in title) & ("副" not in title) & ("助理" not in title):
            self.title = "教授"
        else:
            self.title = title

    def print_expert(self):
        print(self.num, self.name, self.title)
