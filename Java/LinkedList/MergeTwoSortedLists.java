/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class MergeTwoSortedLists {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if(l1 == null){
            return l2;
        }else if(l2 == null){
            return l1;
        }
        int count = 1;
        int count2 = 1;
        ListNode current = l1;
        while(current.next != null){
            count++;
            current = current.next;
        }

        current = l2;
        while(current.next != null){
            count2++;
            current = current.next;
        }

        int[] arr = new int[count+count2];
        current = l1;
        for(int i=0; i < count; i++){
            arr[i] = current.val;
            current = current.next;
        }
        current = l2;
        for(int i=count; i < count+count2; i++){
            arr[i] = current.val;
            current = current.next;
        }
        Arrays.sort(arr);
        ListNode node = new ListNode(arr[arr.length-1]);
        current = node;
        for(int i = arr.length-2; i >= 0; i--){
            ListNode n = new ListNode(arr[i]);
            n.next = current;
            current = n;
        }
        return current;
    }
}