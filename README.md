#Weather checker
Данная программа позволяет узнать температуру в городах России, причем при повторном запросе в течении 5 минут информация берется из кэша.
##Постановка задачи:
Нужно написать консольное приложение, которое по входному параметру с названием города будет показывать в простом текстовом виде текущую погоду в градусах цельсия.
##Запуск программы:
Перейдите в директорию программы в вашей консоли и запустите:

> python -m weather city
## Использованные библиотеки:

+ typer
+ requests
+ BeautifulSoup from bs4
+ time
+ pickle