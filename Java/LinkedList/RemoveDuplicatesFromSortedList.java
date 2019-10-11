public class RemoveDuplicatesFromSortedList {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode current = head;
        if(current == null){
            return current;
        }
        List<Integer> l = new ArrayList<Integer>();
        while(current != null){
            if (!l.contains(current.val)){
                l.add(current.val);
            }
            current = current.next;
        }
        current = null;
        for(int i = l.size()-1; i >=0; i--){
            ListNode n = new ListNode(l.get(i));
            n.next = current;
            current = n;
        }
        return current;
    }
}
