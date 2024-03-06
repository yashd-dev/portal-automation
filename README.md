# Automated Feedback Submission Script For Portal

## Requirements:
- Python 3.x
- Selenium WebDriver
- Chrome WebDriver (chromedriver)
- Chrome Browser

## Installation:
1. Ensure you have Python 3.x installed on your system.
2. Create a virtual environment to manage dependencies. Open a terminal/command prompt and navigate to the directory containing the script.

   ```
   python -m venv env
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     env\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source env/bin/activate
     ```

4. Install the required packages within the virtual environment:

   ```
   pip install -r requirements.txt
   ```
   Replace `requirements.txt` with a file containing the required dependencies (`selenium`, `chromedriver`, etc.).

## Usage:
1. Make sure the virtual environment is activated.
2. Put your SAP ID and password in the `main.py` file.
3. Change the `feedback_url` variable to the URL of the feedback form.
4. Change the Number of pages in the `main.py` file. It's the first loop in the `main` function.
5. Change the number of faculty members in the `main.py` file. It's the second loop in the `main` function.
6. Run the script using the command:
    ```
    python main.py
    ```

## Script Flow:
1. The script launches a Chrome browser window and navigates to the SVKM portal login page.
2. It inputs the SAP ID and password provided in the script to log in.
3. After a delay of 20 seconds to allow for manual login if needed, it navigates to the feedback form URL.
4. The script iterates through the feedback form, providing random ratings for each faculty member.
5. Once all feedback is submitted, it clicks the submit button.
6. The script repeats this process for each page of the feedback form.
7. After completing all pages, it exits after a delay of 10 seconds.

## Important Note:
- Ensure that you have a stable internet connection while running the script.
- Make sure to review and adjust the script as necessary before running, especially if there are changes to the web page structure.

## Disclaimer:
- This script is intended for educational purposes only and should not be used for any unethical or illegal activities. The author is not responsible for any misuse of this script.
- Use this script at your own risk and discretion.
- The author does not endorse or promote any unethical or illegal activities.
- The author is not responsible for any consequences of using this script for unethical or illegal activities.
- The author does not take any responsibility for any action taken against the user for using this script for unethical or illegal activities.
- The author does not take any responsibility for any damage caused by this script to any system or entity.
- By using this script, you agree to the above terms and conditions.

## Issues:
- If you encounter any issues or have any suggestions for improvement, please feel free to open an issue or pull request on the GitHub repository.