# 계산기 만들기
# 함수 : 덧셈, 뺄셈, 메인
def sum_value(x,y):
    return x + y
def sub_value(x,y):
    return x - y


while True:
    print("== 덧셈뺄셈 계산기 **")
    num1 = int(input("수1: "))
    pm = input("연산자(+,-): ")
    num2 = int(input("수2: "))

    if pm == "+":
        result = sum_value(num1, num2)
    elif pm == "-":
        result = sub_value(num1, num2)
    print(f"계산 : {num1} {pm} {num2} = {result}")
    break
    
    # 6. 변수의 범위
    # - 벼눗가 참조 가능한 코드상의 범위를 명시
    # - 함수내의 변수는 자신이 속한 코드 블록이 종료되면 소멸
    # - 이렇게 특정 코드블록에서 선언된 변수를 지역변수
    # - 반대로 가장 상단에 정의되어 프로그램 종료 전까지 유지되는 변수를 전역변수
    # - 같은 이름의 지역변수와 전역변수 존재하는 경우 가까운 (지역변수) 우선 순위가 높음
    num1 = 10 # 전역
    num2 = 20 # 전역

    def test(num1, num2):
        print(num1, num2)
        return
    test(30, 40)
    print(num1, num2)

    # *함수 내에서 함수밖의 전역변수를 변경하고 싶은 경우
    # 1.return 반환값
    a = 1
    print(a)
    def vartest(a):
        a= a+1
        return a
    a = vartest(3)
    print(a)

    # 2. global 키워드 (절대 사용 금지)
    a=1
    print(a)
    def vartest():
        global a
        a= a+1
vartest()
print(a)

# 7. variable length parameter(가변길이인자)
# - 전달되는 parameter의 개수가 고정적이지 않은 경우
# - print(), format()
# ex) print("Hi"), print("Hi", "Hello")

# 1) *args: tuple type
def test(*args):
    for item in args:
        print(item)
test(10, 20, 30)
# 2) **kwargs: dict type
def test2(**kwargs):
    for key, value in kwargs.item():
        print(key, value)
test2(a=1, b=2, c=3)