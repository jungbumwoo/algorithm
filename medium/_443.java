class Solution {
    public int compress(char[] chars) {
        int count = 1;
        char lastChar = chars[0];
        int cursor = 0;

        for (int i = 1; i < chars.length; i++) {

            if (chars[i] == lastChar) {
                count++;
                continue;
            }

            chars[cursor] = lastChar;
            cursor += 1;
            lastChar = chars[i];

            if (count != 1) {
                String digits = String.valueOf(count);
                for (int j = 0; j < digits.length(); j++) {
                    chars[cursor] = digits.charAt(j);
                    cursor += 1;
                }   
            }
            
            count = 1;
        }

        chars[cursor] = lastChar;
        cursor += 1;
        if (count != 1) {
            String digits = String.valueOf(count);
            for (int j = 0; j < digits.length(); j++) {
                chars[cursor] = digits.charAt(j);
                cursor += 1;
            }
        }
        
        return cursor;
    }
}