with open("data.txt", "r") as g:
    text = [str(x) for x in g.read() ]
    print(text)
    exit()
    with open("clean_data.txt", "w") as cd:
        cd.write(*text)
# # from os import path, remove
# # #
# # # remove("text.txt")
# # if not path.exists("text.txt"):
# #      with open("text.txt", "a") as f:
# #           f.write("something\n")
# # else:
# #      with open("text.txt", "w") as f:
# #           f.write("something new\n")
# #
# #
# #
# #
# #
# #
# #
# # # with open("output.txt", "a") as filename:
# # #      filename.write("message\n")
# # # a = open("output.txt", "r")
# # # print(a.read())
# # # a.close()
# # # with open("data.txt", "a") as pesho:
# # #      while True:
# # #           a = input()
# # #           if a == "END":
# # #                break
# # #           else:
# # #                pesho.write(a+ "\n")
# # # a = open("data.txt", "r")
# # # print(a.read())
# # #
# # #
# # #
# # #
# # #
# # #
# with open("numbers.txt", "w") as f:
#      for i in range(1, 11):
#           f.write(str(i) +"\n")
