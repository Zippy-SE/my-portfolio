package Java;

public class LizzieBorden {
    public static void main(String[] args) {
        int parents, whacks, motheraxwhacks, fatheraxwhacks;
        String firstname, lastname, fullname;
        parents = 2;
        whacks = 20;
        motheraxwhacks = parents * whacks;
        fatheraxwhacks = motheraxwhacks + 1;
        firstname = "Lizzie";
        lastname = " Borden";
        fullname = firstname + lastname;  
        System.out.println(fullname + " had an ax, gave her mother " + motheraxwhacks);
        System.out.println("whacks. When she saw what she had done, gave her");
        System.out.println("father " + fatheraxwhacks); 
    }
}           

/*
 # compile
javac c:\my-portfolio\Java\LizzieBorden.java

# run (note package name must be used)
java -cp c:\my-portfolio Java.LizzieBorden
 
*/
       