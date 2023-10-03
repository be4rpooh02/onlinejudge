def solution(letter):
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    
    answer = ''.join([chr(morse.index(ch)+ord('a')) for ch in letter.split()])
    return answer