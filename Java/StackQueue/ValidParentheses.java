public class ValidParentheses {
    public boolean isValid(String s) {
        Map m = new HashMap();
        m.put('(', 1);
        m.put('[', 2);
        m.put('{', 3);
        m.put(')', 1);
        m.put(']', 2);
        m.put('}', 3);
        Stack<Character> S = new Stack<Character>();
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == '(' || s.charAt(i) == '[' || s.charAt(i) == '{'){
                S.push(s.charAt(i));
            }else{
                if(!S.isEmpty()){
                    if(m.get(s.charAt(i)) == m.get(S.peek())){S.pop();}
                    else{return false;}
                }else{
                    return false;
                }

            }
        }
        return S.isEmpty();
    }
}
