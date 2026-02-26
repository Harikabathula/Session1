import java.util.*;
/**
 *
 * @author Hp
 */
public class NewClass2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Map<String, Double> expenses = new HashMap<>();

        while (true) {
            System.out.print("Enter category (or exit): ");
            String category = sc.nextLine();
            if (category.equalsIgnoreCase("exit")) break;

            System.out.print("Enter amount: ");
            double amount = sc.nextDouble();
            sc.nextLine();

            expenses.put(category, expenses.getOrDefault(category, 0.0) + amount);
        }

        System.out.println("\nExpense Summary:");
        for (String key : expenses.keySet()) {
            System.out.println(key + " : " + expenses.get(key));
        }
        sc.close();
    }
}
