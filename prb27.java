package Euler;

public class prb27 {
	
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
	
	public static void main(String[] main) {
		//checkPrime(67);
		int maxa = -1; int maxb = -1; int maxn = -1;
		for(int a = -999; a<=999;a++) {
			for(int b = -1000; b<=1000;b++) {
				int n = consecutiveN(a,b);
				if(n>maxn) {
					maxn = n; maxa= a; maxb = b;
				}
			}
			if(a%10==0)System.out.println(maxn);
		}
		System.out.println(maxa*maxb);
	}

}
