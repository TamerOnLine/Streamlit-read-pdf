# PDF Explorer: Streamlit-powered PDF Reader

An interactive Streamlit application designed to extract and display content from PDF files in an intuitive and user-friendly interface. This project simplifies reading PDFs by enabling users to upload files, view their contents, and perform basic text extraction directly in a web-based environment.

---

## Features

- **Upload PDFs**: Easily upload PDF files using the Streamlit interface.
- **Content Display**: View the content of each page of the uploaded PDF.
- **Text Extraction**: Extract text from PDFs for analysis or further processing.
- **Interactive Interface**: A clean, responsive interface built with Streamlit.
- **Cross-Platform**: Runs seamlessly on Windows, macOS, and Linux.

---

## Screenshots

![Screenshot of the interface](./img/index.png)

---

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.8+**
- Install the required dependencies (see below).

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/TamerOnLine/Streamlit-read-pdf.git
   cd Streamlit-read-pdf
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   streamlit run src/main.py
   ```

5. Open your browser and navigate to `http://localhost:8501`.

---

## Usage

1. Launch the app using the installation steps.
2. Upload your desired PDF file through the interface.
3. View and interact with the extracted content directly in the application.

---

## Development

### Folder Structure

```
Streamlit-read-pdf/
├── src/
│   └── main.py          # Main application file
├── requirements.txt    # List of Python dependencies
├── README.md           # Documentation file
├── venv/               # Virtual environment folder
└── .gitignore          # Git ignore file
```

### How to Contribute

1. Fork this repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Added feature-name"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---

## Contact

For further inquiries or contributions, reach out:

- **Email**: [info@tameronline.com](mailto:info@tameronline.com)
- **GitHub**: [TamerOnLine](https://github.com/TamerOnLine)

---

## Acknowledgements

- Thanks to the Streamlit community for their continuous support and resources.
- Inspired by the simplicity of interactive PDF readers.

---

Enjoy using PDF Explorer! Feel free to share feedback or report issues on the [GitHub Issues page](https://github.com/TamerOnLine/Streamlit-read-pdf/issues).
