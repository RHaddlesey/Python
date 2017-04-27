#Dr R Haddlesey April 2017

answer = input("Do you think we are about to witness a skills gap post Computer Science GCSE?\n")
if answer in ("YES", "Yes", "yes", "yeah", "definitely"):
    print ("I completely agree, in fact I have written a short article about it\n")
    print ("Would you like to read the blog?")
else:
    response = input("Please tell me why you think not...\n")
    print (response)

