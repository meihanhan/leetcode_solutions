public class RemoveLinkedListElements {
    public ListNode removeElements(ListNode head, int val) {
        ListNode current = head;
        head = null;
        while(current != null){
            if(current.val != val){
                ListNode n = new ListNode(current.val);
                n.next = head;
                head = n;
            }
            current = current.next;
        }
        if(head == null || head.next == null){return head;}
        ListNode preNode = null;
        ListNode nextNode = null;
        while(head != null){
            nextNode = head.next;
            head.next = preNode;
            preNode = head;
            head = nextNode;
        }
        return preNode;
    }
}
