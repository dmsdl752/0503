import pickle

def main():
    address_book ={} 				# 공백 딕셔너리를 생성한다.
    while True :
        user = display_menu();
        print("-"*40)
        if user ==1 :
            name, number = get_contact()
            address_book[name]= number		# name과 number를 추가한다.
        elif user ==2 :
            name, number = get_contact()
            address_book.pop(name)		# name을 키로 가지고 항목을 삭제한다.
        elif user ==3 :
            target = input("검색어: ")
            try:
                print(f"{target}의 전화번호: {address_book[target]}")
            except:
                print("검색 실패!")
        elif user ==4 :
            for key in sorted(address_book):
               print(key,"의 전화번호:", address_book[key])
            print("-"*40)
        elif user ==5 : # save
            with open('./saveData.bin', 'wb') as f:
                pickle.dump(address_book, f)
            print("데이터를 저장했습니다.")
        elif user ==6 : # load
            try:
                with open('./saveData.bin', 'rb') as f:
                    address_book = pickle.load(f)
                print("데이터를 불러왔습니다.")
            except:
                print("데이터 로드에 실패했습니다.")
        else :
            break

# 이름과 전화번호를 입력받아서 반환한다.
def get_contact():
    name =input("이름: ")
    number =input("전화번호: ")
    print("-" * 40)
    return name, number			# 튜플로 반환한다.

# 메뉴를 화면에 출력한다.
def display_menu() :
   print("1. 연락처 추가")
   print("2. 연락처 삭제")
   print("3. 연락처 검색")
   print("4. 연락처 출력")
   print("5. 데이터 저장")
   print("6. 데이터 불러오기")
   select = int(input("메뉴 항목을 선택하시오: "))
   return select

main()