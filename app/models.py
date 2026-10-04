#dh file mas2ol 3n el validation w el data models 
from pydantic import BaseModel
#hena bn3ml import l basemodel mn pydantic library 
#basemodel dh class gahz mn pydantic bnst5dmo ka base 3lshan n3ml mno el models bta3tna

class User(BaseModel):
#bn3rf user model ymathl shakl byanat el user eli el API mtwk3ahaS
#y3ny user b2a model mn pydantic w pydatnic y2dr yt2kd en el data eli da5la mashia 7asb el shakl eli m7ddino
#Basemodel=el asas eli bnbny 3lih datamodel bta3tna
    name: str
#name lazm ykon mawgod w no3o string
    email: str
#email lazm ykon mawgod w no3o string