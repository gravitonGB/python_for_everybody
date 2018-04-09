#Exercise 6.5
#print("Excercise 6.5")
text = "X-DSPAM-Confidence:    0.8475";
pos = text.find(':')
t2 = text[pos+1:len(text)]
last_text = t2.strip()
last_value = float(last_text)
print(last_value)
