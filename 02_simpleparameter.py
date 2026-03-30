from fastapi import FastAPI
from enum import Enum

app=FastAPI()
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

class Role(str, Enum):
    admin = "admin"
    user  = "user"
    guest = "guest"

@app.get("/roles/{role}")
def get_by_rule(role:Role):
    return {"role":role,"access":role==Role.admin}
@app.get("orgs/{orgs}/user/{user_id}")
def mutirule(orgs:int,user_id:int):
    return {f"the organaization was done by {orgs} and used by the {user_id}"}
#based on the role i need to talk
@app.get("/roles")
def roles(role:Role):
    if role==Role.admin:
        return "you have all permition"
    elif role==Role.user:
        return "you have the limited access"
    elif role==Role.user:
        return "you have the only the limited access"







"""Good choice — Enum in FastAPI is one of those things that looks simple but unlocks real access control patterns. Let me build it around a real project scenario you'd actually ship.
  ::view-transition-group(*),
  ::view-transition-old(*),
  ::view-transition-new(*) {
    animation-duration: 0.25s;
    animation-timing-function: cubic-bezier(0.19, 1, 0.22, 1);
  }
VvisualizeVvisualize show_widgetGo through all 5 tabs — each one builds on the previous.
The core thing to understand: the Enum does three jobs at once.
Validation — FastAPI rejects any value not in the Enum automatically. You hit GET /roles/superuser and you get a 422 error with "value is not a valid enumeration member" — without writing a single if-check.
Self-documentation — Swagger UI (/docs) shows a dropdown with only the valid values. No one has to guess what's allowed.
Type safety — you compare role == Role.admin, never role == "admin". If you typo it as Role.adimn, Python throws an AttributeError immediately during development, not silently at runtime.
The production pattern in the "Role guard" tab (require_role() as a dependency factory) is exactly how real apps handle this — your route just declares what it needs in one line, and FastAPI + Depends handles the rest. That's what makes FastAPI route code clean and readable at scale."""