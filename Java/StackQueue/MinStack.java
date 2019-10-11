public class MinStack {
    // private Stack<Integer> s;
    private List<Integer> l;
    private int size;
    /** initialize your data structure here. */
    public MinStack() {
        // Stack<Integer> s = new Stack<Integer>();
        l = new ArrayList<Integer>();
        size = 0;
    }

    public void push(int x) {
        l.add(x);
        size++;
    }

    public void pop() {
        l.remove(size-1);
        size--;
    }

    public int top() {
        return l.get(size-1);
    }

    public int getMin() {
        int min = l.get(0);
        for(int i = 1; i < size; i++){

            min = Math.min(l.get(i), min);
        }
        return min;
    }
}
