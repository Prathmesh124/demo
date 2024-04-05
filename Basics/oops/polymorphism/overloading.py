class abc:
    def run(self):
        print("abc")
    
    def run(self):
        print("abc is way")



class test(abc):

    def run(self):
        print("dfbsdjfv")
        super().run()
a1=test()
a1.run()