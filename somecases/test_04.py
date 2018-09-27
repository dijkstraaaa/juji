import requests
import unittest


class TokenClass(unittest.TestCase):
    def setUp(self):
        self.headers={'Content-Type':'application/json;charset=UTF-8',
                      'User-Agent':'*****',
                      'Accept-Version':'**'}
        self.url='https://blog.csdn.net/qq_39208536/article/details/79378151'

    def getToken(self):
        data={
            'password':'*****',
            'username':'***',
            'role':'***',
            'mall_id':'**'
        }
        self.r=requests.post(self.url+'*/login',json=data,headers=self.headers)
        return {'token':self.r.json()['data']['token'],'cookies':self.r.cookies.get_dict()}

    def test_getInfo(self):
        self.getToken()
        self.r=requests.post(self.url+'*infoGet',json=self.getToken(),headers=self.headers)
        print(self.r.json())

    def tearDown(self):
        pass


if __name__ == '__main__':
    suite=unittest.TestLoader().loadTestsFromTestCase(TokenClass)
    unittest.TextTestRunner(verbosity=2).run(suite)