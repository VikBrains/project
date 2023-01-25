helper = str("Алиса")
print("Я – Ваш помощник", helper)
user_name = input("Введите Ваше имя:  ")
user_age = int(input("Введите Ваш возраст:  "))
user_job = int(input("С какого возраста Вы в IT?  "))
job_start = (user_age - user_job)
rest = input(f"{user_name}, Вы пишете на Python {job_start} лет? ")
if rest == "да":
    print("Ok, Вы с нами!")
if rest != "да":
    print("Извините")
