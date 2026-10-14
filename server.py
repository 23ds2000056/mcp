import hashlib
from fastmcp import FastMCP
from fastmcp.server.dependencies import get_http_headers

EMAIL="23ds2000056@ds.study.iitm.ac.in"

mcp=FastMCP("Exam Mcp Server")

@mcp.tool
def solve_challenge() -> str:
        """ Return the required hash for exam challenge."""
        headers=get_http_headers(include_all=True)
        challenge=headers.get("x-exam-challenge")
        if not challenge:
                raise ValueError("Missing exam challenge error.")

        data=f"{challenge}:{EMAIL}".encode("utf-8")
        digest=hashlib.sha256(data).hexdigest()
        return digest[:16]

if __name__=="__main__":
        mcp.run(transport="http",host="0.0.0.0",port=8000,path="/mcp")
