import pytest
class Test_capstone:
    @pytest.mark.parametrize("num,result",[(10,[1,2,5,10]),(1,[1]),(2,[1,2])])
    def test_factorial(self,num,result):
        l1=[]
        for i in range (1,num+1):
            if num%i == 0:
                l1.append(i)
        if result==l1:
            assert True
        else:
            assert False
    @pytest.mark.parametrize("s,result",[("hcl","lch"),("group","puorg")])
    def test_reversestring(self,s,result):
        s1=s[::-1]
        if s1==result:
            assert True
        else:
            assert False
    @pytest.mark.parametrize("list,list1", [([100, 39, 79, 80, 36], [100, 80, 79, 39, 36])])
    def test_sort(self,list, list1):
        list2 = sorted(list, reverse=True)
        if list2 == list1:
            assert True
        else:
            assert False
    @pytest.mark.parametrize("l,result",[([0,7,8,9],8)])
    def test_seclargest(self,l,result):
        l1=list(set(l))
        l2=sorted(l1)
        if l2[-2]==result:
            assert True
        else:
            assert False

