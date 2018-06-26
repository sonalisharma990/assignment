#Q1
import re
emails="zuck26@facebook.com" "page33@google.com" "jeff42@amazon.com"
pattern=r'(\w+)@([A-Z0_9]+)\.([A-Z]{2,4})'
print(re.findall(pattern,emails,flags=re.IGNORECASE))


#Q2
import re
text="Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
match=re.findall(r'\bB\w+',text,flags=re.IGNORECASE)
print(match)


#Q3
import re
irregular_sentence="A, very very; irregular_sentence"
regular_sentence=re.compile("[,;_]")
regular_sentence1=regular_sentence.sub("",irregular_sentence)
print(regular_sentence1)



#Q4
tweet='''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
def clean_tweet(tweet):
    tweet=re.sub('http\S+\s*', " ",tweet)
    tweet=re.sub('RT|cc', " ", tweet)
    tweet=re.sub('#\S+', " ", tweet)
    tweet=re.sub('@\S+', " ", tweet)
    tweet=re.sub('[%s]'%re.escape("""!"#&$%'()*+,-.\:;<=>?@[\]^_'{|}~"""), " ",tweet)
    tweet=re.sub('\s+', " ",tweet)
    return tweet
print(clean_tweet(tweet))