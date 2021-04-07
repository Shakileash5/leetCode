class Solution:
    def reverseBits(self, n: int) -> int:
        #print(bin(n))
        def dec_to_bin(x):
            return int(bin(x)[2:])
        def binaryToDecimal(n):
                num = n;
                dec_value = 0;

                # Initializing base
                # value to 1, i.e 2 ^ 0
                base1 = 1;

                len1 = len(num);
                for i in range(len1 - 1, -1, -1):
                    if (num[i] == '1'):    
                        dec_value += base1;
                    base1 = base1 * 2;

                return dec_value;
        def binToDec(x):
            temp = int(x)
            decimal = 0
            base = 1
            while(temp):
                lastDigit = temp%10
                temp = int(temp/10)
                
                decimal += lastDigit*base
                base *=2
            return decimal
        
        binary = list(str(dec_to_bin(n)))
        size = len(binary)
        binary = ''.join(binary[::-1])
        
        zerosToAdd = 32-size
        zeros = '0'*zerosToAdd
        binary+=zeros
        #n = binToDec(binary)
        n = binaryToDecimal(binary)
        #n = int(binary,2)
        
        return n