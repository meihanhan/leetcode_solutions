public class MinimumAddToMakeParenthesesValid {
    public int minAddToMakeValid(String S) {
        Stack<Character> s = new Stack<Character>();
        for(int i = 0; i < S.length(); i++){
            if(S.charAt(i) == '('){
                s.push(S.charAt(i));
            }else{
                if(s.isEmpty()){
                    s.push(S.charAt(i));
                }else if(s.peek() != '('){
                    s.push(S.charAt(i));
                }else{
                    s.pop();
                }
            }
        }
        return s.size();
    }
}
