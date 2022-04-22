import java.util.HashMap;
import java.util.Map;

class LRUCache {

    int capacity;
    Map<Integer, Node> store = new HashMap<>();

    Node first;
    Node last;

    public LRUCache(int capacity) {
        this.capacity = capacity;
    }

    public int get(int key) {
        if (store.containsKey(key)) {
            moveFirst(key);
            return store.get(key).value;
        }
        return -1;
    }

    public void put(int key, int value) {
        if (get(key) >= 0) {
            store.get(key).value = value;
            return;
        }
        Node node = new Node();
        node.key = key;
        node.value = value;
        node.next = first;
        if (first != null) {
            first.prev = node;
        }
        first = node;
        if (last == null) {
            last = node;
        }
        store.put(key, node);

        if (store.size() > capacity) {
            deleteLast();
        }
    }

    void moveFirst(int key) {
        Node node = store.get(key);
        if (node.prev != null) {
            node.prev.next = node.next;
            if (node.next != null) {
                node.next.prev = node.prev;
            } else {
                last = node.prev;
            }
            store.remove(key);
            put(key, node.value);
        }
    }

    void deleteLast() {
        Node node = last;
        if (last != null) {
            last = node.prev;
            last.next = null;
            store.remove(node.key);
        }
    }

    class Node {
        Node prev;
        Node next;
        int value;
        int key;
    }

}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */