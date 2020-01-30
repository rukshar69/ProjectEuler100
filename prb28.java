package Euler;

public class prb28 {
	
	static int  solution(int n) {
	    n = (n - 1) / 2; //length of diagonal per quadrant
	    int temp = 8*n*n + 15*n + 13;
	    temp *= 2*n;
	    temp /=3;
	    temp++;
	    return temp;
	}
	public static void main(String[] args) {
		int soln = solution(1001);
		System.out.print(soln);
	}

}
