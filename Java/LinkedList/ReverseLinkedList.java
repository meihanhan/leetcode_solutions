import java.util.Stack;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class ReverseLinkedList {
    public ListNode reverseList(ListNode head) {
        if (head == null){
            return head;
        }
        ListNode current = head;
        int count = 0;
        Stack<Integer> s = new Stack<Integer>();
        while(current != null){
            count++;
            s.add(current.val);
            current = current.next;
        }
        ListNode n = new ListNode(s.pop());
        current = n;
        head = n;
        while(!s.isEmpty()){
            ListNode node = new ListNode(s.pop());
            current.next = node;
            current = node;
        }
        return head;
    }
}
