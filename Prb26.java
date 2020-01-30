package Euler;

import java.util.*;
public class Prb26 {
	static HashMap<Integer, Integer> remainders;
	static int repeatingLen(int divisor) {
		int tempNum = 1; int step = 0;
		do {
			remainders.put(tempNum, step);
			step++;
			tempNum = (tempNum%divisor) *10;
			
		}while(remainders.get(tempNum)==null);
		
		return step - remainders.get(tempNum);
	}
	
	
	public static void main(String[] args) {
		
		
		//System.out.print(remainders.get(0));
		//int k = repeatingLen(7);
		//System.out.println(k);
		int maximumNumber = -1; int maxlen = -1;
		for(int d = 1;d<1000;d++) {
			 remainders = new HashMap<Integer, Integer>();
			int m = repeatingLen(d);
			System.out.println(m);
			if(maxlen<m) {
				maxlen = m;
				maximumNumber = d;
			}
		}
		
		System.out.println(maximumNumber);
	}

}
