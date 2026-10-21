class Solution {
    public boolean isValid(String s) {
        Map<Character,Character> pairs = new HashMap<>();
        pairs.put('(', ')');
        pairs.put('[', ']');
        pairs.put('{', '}');
        
        Deque<Character> stack = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            if (pairs.containsKey(c)) {
                // open bracket
                stack.push(c);
            }
            else {
                // closed bracket
                if (stack.isEmpty()) {
                    // no existing open brackets 
                    return false;
                }
                if (pairs.get(stack.pop()) != c) {
                    // existing open brackets, check first
                    // pop of stack is the most recent open brakcet
                    return false;
                }            
            }
        }

        if (stack.isEmpty() == false) {
            // still existing open brackets (not enough closing brackets for open b)
            return false;
        }
        return true;
    }
}
