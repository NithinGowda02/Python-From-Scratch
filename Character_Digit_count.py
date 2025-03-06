def count_char(sentence):
    char_count = len(sentence.split())
    digit_count= sum(1 for char in sentence if char.isdigit())
    uppercase_count= sum(1 for char in sentence if char.isupper())
    lowercase_count = sum(1 for char in sentence if char.islower())

    return char_count,digit_count,uppercase_count,lowercase_count

sentence=input("enter a sentence..>>")

char_count,digit_count,uppercase_count,lowercase_count=count_char(sentence)

print("character count : ",char_count)
print("digit count : ",digit_count)
print("uppercase count : ",uppercase_count)
print("lowercase count : ",lowercase_count)