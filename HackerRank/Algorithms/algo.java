/*Suppose you need to generate a random permutation of the first N integers. For example, {4, 3, 1, 5, 2} and {3, 1, 4, 2, 5} are legal permutations, but {5, 4, 1, 2, 1} is not, because one number (1) is duplicated and another (3) is missing. This routine is often used in simulation of algorithms. We assume the existence of a random number generator, r, with method randInt(i, j), that generates inte- gers between i and j with equal probability. Here are three algorithms:

1 Fill the array a from a[0] to a[n-1] as follows: To fill a[i], generate random num-bers until you get one that is not already in a[0], a[1], . . . , a[i-1].

2 Same as above algorithm, but keep an extra array called the used array. When a random number, ran, is first put in the array a, set used[ran] = true. This means that when filling a[i] with a random number, you can test in one step to see whether the random number has been used, instead of the (possibly) i steps in the first algorithm.

3 Fill the array such that a[i]=i+1.Then for(i=1;i<n;i++) swapReferences( a[ i ], a[ randInt( 0, i ) ] );
*/
import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

public class HelloWorld {
    static Random rand = new Random();
   
    
    public static void main(String[] args) {
        algo1(5);
        System.out.println();
        algo3(5);
        
    }
    public static int randInt(int i, int j) {
        return rand.nextInt(j-i+1) + i;
    }
    public static void algo1 (int n) {
        int[] a = new int[n];
        int random;
        for(int i=0; i<n; i++) {
            random = rand.nextInt(n)+1;
            
            for(int j=0; j<i; j++){
                if(random == a[j]){
                    random = randInt(1, n);
                    j = -1;
                }
            }
            a[i] = random;
        }
        System.out.print("algo1 : " + Arrays.toString(a));
    }
    public static void algo3 (int n) {
        int[] arr = new int[n];
        int random_posi;
        for (int i=0; i<n; i++){
            arr[i] = i+1;
        }
        for (int i=1; i<n; i++) {
            random_posi = randInt(0, n-1);
            int temp = arr[i];
            arr[i] = arr[random_posi];
            arr[random_posi] = temp;
        }
        System.out.print("algo3 : " + Arrays.toString(arr));
    }
    
}