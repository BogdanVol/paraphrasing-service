from fastapi import APIRouter, Query, Response
import json
from paraphrasers import ParaphraserMethod1, Paraphrase


router = APIRouter()

TREE_PARAM_DESCRIPTION = "Syntactic tree in the form of a string"
LIMIT_PARAM_DESCRIPTION = "Maximum number of paraphrased texts to return"
DEFAULT_LIMIT = 20

@router.get("/paraphrase")
def paraphrase(tree: str = Query(..., description=TREE_PARAM_DESCRIPTION),
               limit: int = Query(DEFAULT_LIMIT, description=LIMIT_PARAM_DESCRIPTION)):
    paraphraser_method = ParaphraserMethod1()  
    p = Paraphrase(paraphraser_method)

    paraphrases = p.paraphrase_text(tree, limit)  
    response = {'paraphrases': paraphrases}
    response_str = json.dumps(response, indent=4, ensure_ascii=False)
    return Response(content=response_str, media_type="application/json")
