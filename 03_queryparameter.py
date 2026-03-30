from fastapi import FastAPI
app=FastAPI()
@app.get("/query/")
def query(limits:int):
    return {"limits":limits}
#adding the default value to the query parameter
@app.get("/real/")
def query_parametes(limits:int=10):
    return f"{limits}"
"""In FastAPI, skip is commonly used as a query parameter for implementing pagination in API endpoints.

 It specifies the number of records to offset (or skip) from the beginning of a dataset before returning results.

Pagination Basics
FastAPI tutorials often pair skip with a limit parameter to enable efficient data retrieval for large 
collections. For example, skip=0 and limit=10 returns the first 10 items, while skip=10 and limit=10 returns items 11-20"""
@app.skip("/skip/")
def skill(limit:int,skip:int=10):
    return f"this was started from {skip} and end with {skip}"
