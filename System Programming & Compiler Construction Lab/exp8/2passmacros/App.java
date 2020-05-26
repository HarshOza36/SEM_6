import java.util.List;

public class App{
	public static void main(String[] args) {
		TwoPassMacroprocessor twoPassMacroprocessor = new TwoPassMacroprocessor();
        String input_string = "START\n" +
                "\n" +
                "MACRO\n" +
                "ADD &ARG1,&ARG2\n" +
                "L 1,&ARG1\n" +
                "A 1,&ARG2\n" +
                "MEND\n" +
                "\n" +
                "MACRO\n" +
                "SUB &ARG3,&ARG4\n" +
                "L 1,&ARG3\n" +
                "S 1,&ARG4\n" +
                "MEND\n" +
                "\n" +
                "ADD DATA1,DATA2\n" +
                "SUB DATA1,DATA2\n" +
                "\n" +
                "DATA1 DC F'9'\n" +
                "DATA2 DC F'5'\n" +
                "\n" +
                "END";

        List<List<String []>> input = twoPassMacroprocessor.parseInput(input_string);
        twoPassMacroprocessor.generatePasses(input);
        twoPassMacroprocessor.populateALA();
        twoPassMacroprocessor.performPass1();
        twoPassMacroprocessor.performPass2();
    }
}