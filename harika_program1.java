// Creating a expenditure analyzer 
/*
creating a analyzer of expenses with different categories
*/
import java.util.*;

public class harika_program1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Map<String,Double>expenses = new HashMap<>();
        // looping to get category and amount every time from user until the user says exit
        while(true){
            System.out.println(("Enter the category (or exist)"));
            String category = sc.nextLine();
            // if they exist i am using here break
            if (category.equalsIgnoreCase("exist")) break;
            // if they continue taking the expenses of that category
            System.out.println("Enter the amount");
            double amount = sc.nextDouble();
            sc.nextLine();
            expenses.put(category,expenses.getOrDefault(category,0.0)+amount);  
        }
        System.out.println("/n Expenses all in Summary:--");
        for (String key:expenses.keySet() ){
            System.out.println((key+" "+expenses.get(key)));
        }
        sc.close();
    }
}
