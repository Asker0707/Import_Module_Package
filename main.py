from application.salary import calculate_salary
from application.db.people import get_employees 
import datetime
from pretty_table import beautiful_table

#Знакомство с datetime
current_date = datetime.date.today()





if __name__ == "__main__":
    #Задание 1 и 2
    print(calculate_salary())
    print(get_employees())
    
    #Задание 3 знакомство с datetime
    print(current_date)
    
    #задание 4 понравившийся модуль и пример
    beautiful_table()