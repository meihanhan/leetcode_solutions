public class PalindromeLinkedList {
    public boolean isPalindrome(ListNode head) {
        if(head == null){return true;}
        List<Integer> l = new ArrayList<Integer>();
        ListNode current = head;
        while(current != null){
            l.add(current.val);
            current = current.next;
        }
        current = head;
        for(int i = l.size()-1; i >= 0; i --){
            if (l.get(i) == current.val){
                current = current.next;
            }else{
                return false;
            }
        }
        return true;
    }
}
