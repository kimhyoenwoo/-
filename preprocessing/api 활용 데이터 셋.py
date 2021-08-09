import pandas as pd 
import re


#데이터 조회 
bus_stop = pd.read_csv('/content/정류장+승하차+이용정보.csv')
bus_stop.tail()
df = bus_stop.iloc[:2637,]
# print(df)
bus_stop = pd.DataFrame(df)
bus_stop

#정규식 생성 
listed = []
for i in bus_stop_num:
    m = re.findall('\((.*)\)',str(i))
    listed.extend(m)
print(listed)
## ()가 잘 지워지지 않는 오류 발견 

# 정규식 짜서 햇더니 오류 발생. 해결 할 수는 있는데 좀 복잡할듯 간결한 코드 작성 
result = re.findall('\((.*)\)','DCC종점(45320)')
print(type(result))
print(result)
#종점)(53210

#간결한 코드 
first = bus_stop_num[0]
print(first)
print(first[-6:-1])

# 버스 정류장 ars번호 추출 
bus_stop_list = []
for i in range(0,len(bus_stop_num)):
  m = bus_stop_num[i]
  z = m[-6:-1]
  bus_stop_list.append(z)
print(bus_stop_list)
#결측값을 99999로 처리해서 해당 데이터 전처리가필요함 

#99999제거 
bus_list = bus_stop_list.copy()
print(bus_list)
bus_list.remove('99999')
