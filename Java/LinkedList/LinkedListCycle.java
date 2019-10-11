public class LinkedListCycle {
    public boolean hasCycle(ListNode head) {
        if (head == null){return false;}
        ListNode pointer1 = head;
        ListNode pointer2 = head.next;
        while(pointer1 != pointer2){
            if(pointer2 == null || pointer2.next == null){return false;}
            pointer1 = pointer1.next;
            pointer2 = pointer2.next.next;
        }
        return true;
        // ListNode last = head;
        // while(last.next != null){
        //     last = last.next;
        // }
        // last = last;
        // ListNode current = head;
        // while(current != null){
        //     if (last.next == current){
        //         return true;
        //     }
        //     current = current.next;
        // }
        // return false;
    }
}
