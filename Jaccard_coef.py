"""
File Name : Jaccard_coef.py

Inputs : Doc1.txt Doc2.txt

Output : Value of Jaccard similarity coefficient

Implemented By : Sanket Kakad


"""

def main():
  Count = 0;
  Doc1 = open("Doc1.txt", 'r');
  Doc2 = open("Doc2.txt", 'r')
  Doc1_D = {}
  Doc2_D = {}
  DocR_D = {}

  for line in Doc1:
        for word in line.split():
          word_s = word.lower()
          Doc1_D[word_s] = 1
          DocR_D[word_s] = 1

  for line in Doc2:
        for word in line.split():
          word_s = word.lower()
          Doc2_D[word_s] = 1
          DocR_D[word_s] = 1

  Doc1_Set = set(Doc1_D)
  Doc2_Set = set(Doc2_D)
  #print(Doc1_Set)
  #print(Doc1_D)
  for w in Doc1_Set:
    for w1 in Doc2_Set:
      if w==w1:
        #print("hi")
        Count = Count+1
    
          
  print ("Intersection of Document :" + str((Count) )+ "\n" + "Union of Doc :" + str(len(DocR_D)))
  print ("Jaccard similarity coefficient = " +str(Count/len(DocR_D)))
  
  
main()


""" 
OUTPUT :

python  Jaccard_coef.py
Intersection of Document :2
Union of Doc :5
Jaccard similarity coefficient = 0.4

"""