"""

 from collections import Counter
 text = ('to be or not to be that is the question')
 counter = Counter(text.split())
 for word, count in sorted(counter):
  print(f'{word:<12}{count}')

  
The problem is that the code is sorting only the words but trying to unpack both the word and the count.
That’s why it doesn’t work. I need to sort the word–count pairs instead of just the words.
"""