
# results validation, documentation, and automatic ORM objects to JSON conversions. 

from ninja import Schema

from datetime import datetime

# Input Field (PUT, UPDATE)
class PostInputSchema(Schema):
    title: str
    content: str
    



# Output Field (GET)
class PostOutputSchema(Schema):
    id: int
    title: str 
    content: str 
    created: datetime
    