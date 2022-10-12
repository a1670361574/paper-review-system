class Expert:
    def __init__(self, num, name, title):
        self.num = num
        self.name = name
        if ("教授" in title) & ("副" not in title) \
                & ("助理" not in title):
            self.title = "教授"
        else:
            self.title = title
        if "博导" in title:
            self.isPhdTutor = True
        else:
            self.isPhdTutor = False