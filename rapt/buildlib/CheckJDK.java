/**
 * This is a short program that compares the major version of the JDK
 * to its first argument, exiting with 0 if the version is greater or
 * equal, and 1 otherwise.
 */
public class CheckJDK {

    static int versionInt(String s) {
        s = s.split("-")[0];
        s = s.split("\\.")[0];
        return Integer.parseInt(s);
    }

    public static void main(String argv[]) {
        int version = versionInt(System.getProperty("java.version"));
        int target = versionInt(argv[0]);

        System.out.println("Java version: " + version);
        System.out.println("Target version: " + target);

        if (version >= target) {
            System.out.println("OK");
            Runtime.getRuntime().exit(0);
        } else {
            System.out.println("ERROR: Java version is too low");
            Runtime.getRuntime().exit(1);
        }
    }
}
