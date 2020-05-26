
public class App{
	public static void main(String[] args) {
		TwoPassAssembler twoPassAssembler = new TwoPassAssembler();
        String input = "JOHN START 0\n" +
                        "USING *,15\n" +
                        "L 1,FIVE\n" +
                        "A 1,FOUR\n" +
                        "ST 1,TEMP\n" +
                        "FOUR DC F'4'\n" +
                        "FIVE DC F'5'\n" +
                        "TEMP DS 1F\n" +
                        "END";
        System.out.println("Assembly Code: ");
        System.out.println(input + "\n");
        twoPassAssembler.parseInput(input);
        twoPassAssembler.getSpecifics();
        twoPassAssembler.performPass1();
        twoPassAssembler.performPass2();
    }
}