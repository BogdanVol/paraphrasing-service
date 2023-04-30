Rephrase API

Description
The Paraphrase API provides a way to generate paraphrased texts from syntax trees.

Installation
Clone the repository: git clone https://github.com/BogdanVol/paraphrasing-service.git
Navigate to the project directory: cd rephrase_api
Create and activate a virtual environment (optional but recommended):
python3 -m venv venv
For Windows: venv\Scripts\activate
For Unix/macOS: source venv/bin/activate
Install the required dependencies: pip install -r requirements.txt

Usage
Start the server:
uvicorn main:app --reload
Open your web browser and navigate to http://localhost:8000.
Use the API endpoint to paraphrase text:
Endpoint: http://localhost:8000/paraphrase
Method: GET
Query Parameters:
tree (required): Syntactic tree in the form of a string.
limit (optional): Maximum number of paraphrased texts to return (default: 20).
Example Usage:
http://127.0.0.1:8000/paraphrase?tree=(S%20(NP%20(NP%20(DT%20The)%20(JJ%20charming)%20(NNP%20Gothic)%20(NNP%20Quarter)%20)%20(,%20,)%20(CC%20or)%20(NP%20(NNP%20Barri)%20(NNP%20G%C3%B2tic)%20)%20)%20(,%20,)%20(VP%20(VBZ%20has)%20(NP%20(NP%20(JJ%20narrow)%20(JJ%20medieval)%20(NNS%20streets)%20)%20(VP%20(VBN%20filled)%20(PP%20(IN%20with)%20(NP%20(NP%20(JJ%20trendy)%20(NNS%20bars)%20)%20(,%20,)%20(NP%20(NNS%20clubs)%20)%20(CC%20and)%20(NP%20(JJ%20Catalan)%20(NNS%20restaurants)%20)%20)%20)%20)%20)%20)%20)
