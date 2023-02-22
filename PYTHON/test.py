import re
print('----------0214----------')
#sub를 이용해서 : 제거
ch = 'Scene:'
print(re.sub(':', '', ch))
# ch = re.sub(':', '', ch)
# print(ch)

a = '제 이메일 주소는 greate@naver.com'
a += ' 오늘은  today@naver.com 내일은 apple@gmail.com  life@abc.co.kr 라는 메일을 사용합니다.'
print(a)
# 메일주소만 출력하기
# a = re.findall(r'\([a-z].+?\@[a-z].+?\.[a-z].?+|\.[a-z].+?\)', a) 내가쓴 답 ㅠㅠ
a1 = re.findall(r'[a-z]+@[a-z.]+', a)
print('메일주소 :', a1)

words = ['apple', 'cat', 'brave', 'drama', 'asise', 'blow', 'coat', 'above']
# a로 시작하는 단어 출력
mm = []
for i in words:
    mm += re.findall(r'a[a-z]+', i) # a로 시작하는 단어 : ['ap', 'at', 'av', 'am', 'as', 'at', 'ab']이 출력됨
print('a로 시작하는 단어 :', mm)
print()

for i in words:
    m = re.search(r'a[a-z]+', i)
    if m:
        print('search :', m.group())
# print('search :', m)

# match 사용해보자 
for i in words:
    # m = re.match(r'a[a-z]+', i) 
    m = re.match(r'a\D+', i)  # \d 숫자  \D 숫자아닌
    if m:
        print('match :', m.group())
# print('match :', m)