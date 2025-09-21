class Utilitymethods():
    def oddorEven():
        num = int(input("enter the age"))
        if(num%2==1):
            print("odd")
            message = "Odd number"
        else:
            print("even")
            message = "Even number"
        return message
    def ageCategoryNoReturn():    
        if(age<18):
            print("children")
            cate = "children"
        elif(age<35):
            print("Adult")
            cate = "Adult"
        elif(age<59):
            print("citizen")
            cate = "citizen"
        else:
            print("senior citizen")
            cate = "senior citizen"
        return cate