/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class MiddleOfTheLinkedList {
    public ListNode middleNode(ListNode head) {
        ListNode current = head;
        int count = 0;
        while(current.next != null){
            count++;
            current = current.next;
        }
        count ++;
        int i = 0;
        for (; i < count; i++){
            if (i >=  count / 2){
                break;
            }
            head = head.next;
        }

        return head;
    }
}