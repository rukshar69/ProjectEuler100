package Euler;

public class prb27_v2 {

	
static boolean isPrime(int num) {
		if(num<2) return false;
		if(num%2 ==0) if(num==2) return true; else return false;
		if(num%3 ==0) if(num==3) return true; else return false;
		
		int limit = 1 + (int)Math.sqrt(num);
		int i = 5;
		while(i<=limit) {
			if(num%i==0 || num%(i+2) ==0) return false;
			i+=6;
		}
		return true;
	}
	
	static void checkPrime(int num) {
		if(isPrime(num))System.out.print("Y"); else System.out.print("N");
	}
	
	static int consecutiveN(int a , int b) {
		int count = 0; boolean flag = true; int n = 0;
		while(flag) {
			int num = n*n + a*n + b;
			if(isPrime(num)) {
				count++; n++;
			}
			else break;
		}
		return count;
	}
	
	
	
	static int [] primeNumbers;
	
	static void sieveOfEratosthenes(int n) 
    { 
        // Create a boolean array "prime[0..n]" and initialize 
        // all entries it as true. A value in prime[i] will 
        // finally be false if i is Not a prime, else true. 
        boolean prime[] = new boolean[n+1]; 
        for(int i=0;i<n;i++) 
            prime[i] = true; 
          
        for(int p = 2; p*p <=n; p++) 
        { 
            // If prime[p] is not changed, then it is a prime 
            if(prime[p] == true) 
            { 
                // Update all multiples of p 
                for(int i = p*2; i <= n; i += p) 
                    prime[i] = false; 
            } 
        } 
          
        // Print all prime numbers 
        int c = 0;
        for(int i = 2; i <= n; i++) 
        { 
            if(prime[i] == true) 
                c++;
        } 
        primeNumbers = new int[c];
        int index = 0;
        for(int i = 2; i <= n; i++) 
        { 
            if(prime[i] == true) {
            	primeNumbers[index] = i; index++;
            }
            	
        } 
        
    } 
	
	public static void main(String[] main) {
		//checkPrime(67);
		
		
		sieveOfEratosthenes(1000);
		int [] primes = primeNumbers;
		
		
		int maxa = -1; int maxb = -1; int maxn = -1; int limit = primes.length;
		System.out.println(limit);
		
		for(int a = -999; a<=999;a++) {
			for(int b = 0; b<primes.length;b++) {
				
				
				int n = consecutiveN(a,primes[b]);
				if(n>maxn) {
					maxn = n; maxa= a; maxb = primes[b];
				}
			}
			//if(a%10==0)System.out.println(maxn);
		}
		System.out.println(maxa*maxb);
		
		
	}
}
