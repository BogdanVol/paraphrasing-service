# Rephrase API
The Paraphrase API provides a way to generate paraphrased texts from syntax trees.
 
## Installation

Clone the repository: git clone https://github.com/BogdanVol/paraphrasing-service.git

Navigate to the project directory: cd rephrase_api

Create and activate a virtual environment (optional but recommended):

- python3 -m venv venv

- For Windows: venv\Scripts\activate

- For Unix/macOS: source venv/bin/activate

Install the required dependencies: pip install -r requirements.txt

## Usage

Start the server:

- uvicorn main:app --reload

Open your web browser and navigate to http://localhost:8000

Use the API endpoint to paraphrase text:

Endpoint: http://localhost:8000/paraphrase
Method: GET
Query Parameters:
- tree (required): Syntactic tree in the form of a string.
- limit (optional): Maximum number of paraphrased texts to return (default: 20).
## Example Usage:
http://127.0.0.1:8000/paraphrase?tree=(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP
Quarter) ) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic) ) ) (, ,) (VP (VBZ has) (NP (NP
(JJ narrow) (JJ medieval) (NNS streets) ) (VP (VBN filled) (PP (IN with) (NP (NP (JJ
trendy) (NNS bars) ) (, ,) (NP (NNS clubs) ) (CC and) (NP (JJ Catalan) (NNS
restaurants) ) ) ) ) ) ) )
