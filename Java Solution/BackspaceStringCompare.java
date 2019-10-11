public class BackspaceStringCompare {
    public boolean backspaceCompare(String S, String T) {
        Stack<Character> ss = new Stack<Character>();
        Stack<Character> st = new Stack<Character>();
        for(int i = 0; i < S.length(); i++){
            if(S.charAt(i) == '#'){
                if(!ss.isEmpty()){
                    ss.pop();
                }
            }else{
                ss.push(S.charAt(i));
            }
        }
        for(int i = 0; i < T.length(); i++){
            if(T.charAt(i) == '#'){
                if(!st.isEmpty()){
                    st.pop();
                }
            }else{
                st.push(T.charAt(i));
            }
        }
        while(!ss.isEmpty() && !st.isEmpty()){
            if(ss.pop()!= st.pop()){
                return false;
            }
        }
        return ss.isEmpty() && st.isEmpty();
    }
}
