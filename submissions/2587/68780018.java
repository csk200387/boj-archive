public class Main {
  public static void main(String[] args) {
    int[] arr = new int[5];
    int sum = 0;
    for (int i = 0; i < 5; i++) {
      arr[i] = Integer.parseInt(System.console().readLine());
      sum += arr[i];
    }
    bubbleSort(arr);
    System.out.println(sum / 5);
    System.out.println(arr[2]);
  }

  public static void bubbleSort(int[] arr) {
    for (int i = 0; i < arr.length - 1; i++) {
      for (int j = 0; j < arr.length - i - 1; j++) {
        if (arr[j] > arr[j + 1]) {
          int temp = arr[j];
          arr[j] = arr[j + 1];
          arr[j + 1] = temp;
        }
      }
    }
  }
}