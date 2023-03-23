import os
print(os.getcwd()) #C:\Users\Admin\Desktop\Github\ITSTEPHW\Practice
first = os.path.abspath(os.path.dirname(__file__))  # содержит абсолютный путь к текущему скрипту
print(first) #C:\Users\Admin\Desktop\Github\ITSTEPHW\Practice
second = "temp\\tempjunk2.txt"  # \ - изоляция символа   \n - перенос строки, \t - табуляция
third = r"temp\junk2.txt"  # \ - изоляция символа   \n - перенос строки, \t - табуляция...
fourth = "temp/junk2.txt"  # \ - изоляция символа   \n - перенос строки, \t - табуляция...
print(second)
path = os.path.join(second, third)  # склеивает несколько путей, корректным образом для каждой системы
print(f"path: {path}")
#TODO Методы
## os.remove("../")
# os.remove("junk.txt")  # remove file
# os.rmdir("junk")  # этим способом можно удалить только пустую папку
# shutil.rmtree("junk")  # этим способом можно удалить папку