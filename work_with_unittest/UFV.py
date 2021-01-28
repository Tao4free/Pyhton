class UFV:
    def __init__(self, name):
        self.name = name
        self.status = 'r0'
        self.reason = ''
        self.run_list = [
                         self.r1,
                         self.r2
        ]

    def mk_gcs_env(self):
        self.blob = 'blob'

    def r1(self):
        self.status = 'r1'
        self.reason = 'r_r1'
        self.r1 = 'r1'
        print('self.r1: ', self.r1)

    def r2(self):
        self.status = 'r2'
        self.reason = 'r_r2'
        self.r2 = 'r2'
        print('self.r1: ', self.r2)

    def run(self):
        self.mk_gcs_env()
        for r in self.run_list:
            r()
        print(self.status)
        print(self.reason)
