public class RemoveOutermostParentheses {
    public String removeOuterParentheses(String S) {
        Stack<Character> s = new Stack<Character>();
        String res = "";
        for(int i = 0; i < S.length(); i++){
            if(S.charAt(i) == '('){
                if(!s.isEmpty()){
                    res += "(";
                }
                s.push('(');

            }else if(S.charAt(i) == ')'){
                s.pop();
                if(!s.isEmpty()){
                    res += ")";
                }
            }
        }
        return res;

    }
}
