from fastapi.responses import JSONResponse

def response_error(message, status_code):
  return JSONResponse(
    content={"error": str(message)},
    status_code= status_code
  )
