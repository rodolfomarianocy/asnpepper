class Faker:
    @staticmethod
    def gen_fake_ips():
        r = []
        for i in range(0,255):
            r.append('10.11.26.' + str(i))
        
        for i in range(0,255):
            r.append('10.11.25.' + str(i))

        for i in range(0,255):
            r.append('10.11.24.' + str(i))

        for i in range(0,255):
            r.append('10.11.23.' + str(i))
        return r

    @staticmethod
    def gen_fake_urls(schema='http://'):
        ips = Faker.gen_fake_ips()
        r = []
        for ip in ips:
            r.append(schema + ip)
        return r