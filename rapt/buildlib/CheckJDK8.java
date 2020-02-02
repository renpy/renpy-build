public class CheckJDK8 {
    public static void main(String argv[]) {
        if (System.getProperty("java.version").startsWith("1.8.")) {
            Runtime.getRuntime().exit(0);
        } else {
            Runtime.getRuntime().exit(1);
        }
    }
}
