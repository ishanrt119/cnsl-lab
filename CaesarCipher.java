import java.util.Scanner;

public class CaesarCipher {
	private static String transform(String text, int key, boolean encrypt) {
		int shift = key % 26;
		if (!encrypt) {
			shift = 26 - shift;
		}

		StringBuilder result = new StringBuilder();

		for (char ch : text.toCharArray()) {
			if (Character.isUpperCase(ch)) {
				result.append((char) ('A' + (ch - 'A' + shift) % 26));
			} else if (Character.isLowerCase(ch)) {
				result.append((char) ('a' + (ch - 'a' + shift) % 26));
			} else {
				result.append(ch);
			}
		}

		return result.toString();
	}

	private static void crackCipher(String text) {
		for (int key = 0; key < 26; key++) {
			String plainText = transform(text, key, false);
			System.out.println("Key " + key + ": " + plainText);
		}
	}

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		System.out.println("Caesar Cipher");
		System.out.println("1. Encrypt");
		System.out.println("2. Decrypt");
		System.out.print("Enter your choice: ");
		int choice = scanner.nextInt();
		scanner.nextLine();

		System.out.print("Enter text: ");
		String text = scanner.nextLine();

		if (choice == 1) {
			System.out.print("Enter key: ");
			int key = scanner.nextInt();
			scanner.nextLine();
			String output = transform(text, key, true);
			System.out.println("Encrypted text: " + output);
		} else {
			System.out.println("Possible decryptions:");
			crackCipher(text);
		}

		scanner.close();
	}
}


