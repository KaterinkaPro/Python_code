# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на 
# новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза
# Input:	5 -> 5 1 6 5 9
# Output:	1 9

N = int(input("Сколько арбузов? "))
list_n = 0
i = 0
min = max = 0
for i in range (N):
  list_n = int(input("Какова масса {i} арбуза "))
  

# while count < N:
#   list_n = int(input("Какова масса арбуза "))

#   count += 1
# if 