public class NextGreaterNodeInLinkedList {
    public int[] nextLargerNodes(ListNode head) {
        ListNode a = head;
        ListNode b = head;
        List<Integer> l = new ArrayList<Integer>();
        while(a != null){
            b = a.next;
            l.add(0);
            while(b != null){
                if (b.val > a.val){
                    l.set(l.size()-1,b.val);
                    break;
                }
                b = b.next;
            }
            a = a.next;
        }
        int[] arr = new int[l.size()];
        for(int i = 0; i < arr.length; i++){
            arr[i] = l.get(i);
        }
        return arr;
    }
}
