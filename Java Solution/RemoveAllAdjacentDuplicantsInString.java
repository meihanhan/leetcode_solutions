import java.util.*;
class RemoveAllAdjacentDuplicantsInString {
    public static void main(String[] args) {
        removeDuplicates("abbaca");
    }
    public static String removeDuplicates(String S) {
        Stack<Character> s = new Stack();
        for(int i = 0; i < S.length(); i++){
            if(s.isEmpty()){
                s.push(S.charAt(i));
            }
            else{
                System.out.println(s.peek()+""+ S.charAt(i));
                if(s.peek() == S.charAt(i)){
                    s.pop();
                }
                else{
                    s.push(S.charAt(i));
                }
            }
        }
        String res = "";
        while(!s.isEmpty()){
            res = s.pop() + res;
        }
        System.out.println(res);
        return res;
    }
}