module FunWithStrings
 
  def palindrome?
    isPalindrome=false
    currentPos=0
    palindromeCheck=self.downcase.gsub(/[^a-z0-9\s]/i, '').gsub(/\s+/, "")
    palArr1=palindromeCheck.chars.to_a
    palArr2=palArr1.reverse
    while isPalindrome == false
      while currentPos <= palArr1.length-1 
       if palArr1[currentPos] != palArr2[currentPos]
       return false
       else
       currentPos += 1
       end 
      end  
      return true   
    end
  end


def count_words
stringToHash=self
stringToHash=stringToHash.downcase
stringToHash=stringToHash.gsub(/[^0-9A-Za-z\s]/, '')
arrToHash=stringToHash.split
wordCount ={}
arrToHash.each do |i|
 if wordCount.include? i
 wordCount[i]+=1
 else 
 wordCount[i]=1  
 end  
end
return wordCount
end  
  
  
  
def anagram_groups
  words = self.downcase.split 
  anagrams = []
  isAnagram=false
    words.each do |wordEnter|
      group = []
      words.each do |wordCheck|
        if wordCheck.length == wordEnter.length
        isAnagram = true
        wordEnter.each_char do |charCheck|
          isAnagram = false unless wordCheck.include? charCheck
        end
        group << wordCheck if isAnagram
        end
      anagrams << group if group.length > 0
    end    
    end
   anagrams
end











end



# make all the above functions available as instance methods on Strings:

class String
  include FunWithStrings
end

# count_words(x)