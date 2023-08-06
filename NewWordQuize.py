print("안녕하세요 신조어 퀴즈 맞추기입니다.")
answer1 = "취향존중"
answer2 = "솔직히까놓고말해서"
answer3 = "케이스바이케이스"
cnt = 0

#print("취존이 어떤 문장의 줄임말인가요?")
#quize1 = input() 
quize1 = input("취존이 어떤 문장의 줄임말인가요?") 
quize1 = quize1.replace(" ","")
if quize1 == answer1:
    print("정답")
    cnt += 1
else :
    print("오답")

print("솔까말이 어떤 문장의 줄임말인가요?")
quize2 = input()
quize2 = quize2.replace(" ","")
if quize2 == answer2:
    print("정답")
    cnt += 1
else :
    print("오답")

print("케바케가 어떤 문장의 줄임말인가요?")
quize3 = input()
quize3 = quize3.replace(" ","")
if quize3 == answer3:
    print("정답")
    cnt += 1
else :
    print("오답")

print("3개 퀴즈 중 "+str(cnt)+"개 정답")