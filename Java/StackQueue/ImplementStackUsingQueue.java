import java.util.LinkedList;
import java.util.Queue;
public class ImplementStackUsingQueue {
    public static void main(String[] args) {

    }
    class MyStack {

        private Queue<Integer> q1 = new LinkedList<>();
        private Queue<Integer> q2 = new LinkedList<>();
        private int temp = 0;

        /**
         * Initialize your data structure here.
         */
        public MyStack() {
        }

        /**
         * Push element x onto stack.
         */
        public void push(int x) {
            q1.add(x);
        }

        /**
         * Removes the element on top of the stack and returns that element.
         */
        public int pop() {
            if (q1.isEmpty()) {
                return q1.remove();
            }
            if (q1.size() == 1) {
                return q1.peek();
            }
            while (q1.size() > 1) {
                q2.add(q1.remove());
            }

            temp = q1.peek();

            while (!q2.isEmpty()) {
                q1.add(q2.remove());
            }
            return temp;
        }

        /**
         * Get the top element.
         */
        public int top() {
            if (q1.isEmpty()) {
                return q1.peek();
            }
            temp = q1.peek();
            if (q1.size() == 1) {
                return temp;
            }
            while (!q1.isEmpty()) {
                if (q1.size() == 1) {
                    temp = q1.peek();
                }
                q2.add(q1.remove());
            }

            while (!q2.isEmpty()) {
                q1.add(q2.remove());
            }
            return temp;

        }

        /**
         * Returns whether the stack is empty.
         */
        public boolean empty() {
            return q1.isEmpty();
        }
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */